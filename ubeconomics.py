# -*- coding: utf-8 -*-
"""
@file
@author  Peter M Bach <peterbach@gmail.com>
@version 1.0
@section LICENSE

This file is part of UrbanBEATS
Copyright (C) 2014  Peter M Bach

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

__author__ = 'Peter M Bach'

"""
WSUD Specification for LCC:
------------------------------
    [WSUD abbreviation] ...
        [SLS] = [System Lifespan (years), major renewal factor (prop. of TCC)]
        [TCC] = [Real construction cost]
        [TAM] = [Annual maintenance cost, maintain during renewal year bool]
        [TRC] = [Real renewal cost, frequency]
        [TDC] = [Total Decommissioning Cost]
    [WSUD abbreviation] ...
"""

def createWSUD_subspec(ls, rf, tcc, tam, tambool, trc, trcfreq, tdc):
    """Creates a dictionary object based on the spec above of a single WSUD system, returns a dictionary of that
    technology's specifications

    :param ls: life span [years] - int
    :param rf: renewal factor as prop. value [ ] - float
    :param tcc: total construction cost [$] - float
    :param tam: total annual maintenance cost [$] - float
    :param tambool: maintain in a renewal year? [ ] - bool
    :param trc: total renewal cost [$] - float
    :param trcfreq: frequency of renewals [years] - int
    :param tdc: total decommissioning cost [$] - float
    :return: A WSUD spec dictionary for a single system
    """
    spec = {}
    spec["SLS"] = [ls, rf]
    spec["TCC"] = [tcc]
    spec["TAM"] = [tam, tambool]
    spec["TRC"] = [trc, trcfreq]
    spec["TDC"] = [tdc]
    return spec



def prepareRealCostMatrix(wsudobj, wsudspec, categories, merge):
    """Scans the real-costs and prepares the real costs array(s) for the LCC exercise

    :param wsudobj: the UrbanBEATS WSUD Object (i.e. the strategy to be costed)
    :param wsudspec: 2D dictionary with keys: [WSUD_abbr.]
    :param categories:
    :param merge:
    :return:
    """


    realcosts = []


    return realcosts


def calculateLCCSimple(realcosts, drates, irates):
    """Calculates the total life cycle cost of the provided real costs and returns the total LCC and EAP as well as the
    annual nominal discounted costs

    :param realcosts:
    :param drates:
    :param irates:
    :return:
    """
    ndcosts = []
    if len(realcosts) == len(drates) and len(realcosts) == len(irates):
        ratesconstant = False
    else:
        print "Discount and inflation rates will not fluctuate over time"
        ratesconstant =  True   #define rates as constant

    nyears = float(len(realcosts) - 1)
    for i in range(len(realcosts)):
        yr = i
        if ratesconstant:
            d = drates[0]
            i = irates[0]
        else:
            d = drates[i]
            i = irates[i]
        ndcosts.append(float((realcosts[i]*(1+i)**yr)/((1+d)**yr)))    #Calculate nominal discounted rate using formula
                                                                # [ Cost * (1+irate)^yr ] / [ (1+drate)^yr ]
    lcc = sum(ndcosts)
    eap = lcc / nyears

    return lcc, eap, ndcosts


def calculateLCCComplex(realcostdict, drates, irates):
    """Calculates the LCC of subsets of real costs based on an input dictionary. This is useful when subcomponents of
    costs need to be split

    :param realcostdict: A dictionary of real cost arrays (keyword = expenditure type
    :param drates: Discount rates, if constant, it is a 1D array of one item
    :param irates: Inflation rate, if constant, it is a 1D array of one item
    :return: A dictionary with each key containing
    """
    cost_components = realcostdict.keys()
    ndcostdict = {}

    for key in cost_components:
        lcc, eap, ndcosts = calculateLCCSimple(realcostdict[key], drates, irates)
        ndcostdict[key] = [lcc, eap, ndcosts]

    return ndcostdict
