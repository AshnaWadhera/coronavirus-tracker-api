"""app.routers.v1.py"""
from fastapi import APIRouter

from ..services.location.jhu import get_category

V1 = APIRouter()


@V1.get("/all")
async def all_categories():
    """Get all the categories."""
    var_list = ['confirmed','deaths','recovered']
    result_dict = {'latest':{}}
    result_op = await get_category(var_list)
    for each_category in result_op:
        result_dict[each_category] = result_op[each_category]
        result_op['latest'][each_category] = result_op[each_category]['latest']
    
    return result_op

@V1.get("/confirmed")
async def get_confirmed():
    """Confirmed cases."""
    confirmed_data = await get_category("confirmed")

    return confirmed_data


@V1.get("/deaths")
async def get_deaths():
    """Total deaths."""
    deaths_data = await get_category("deaths")

    return deaths_data


@V1.get("/recovered")
async def get_recovered():
    """Recovered cases."""
    recovered_data = await get_category("recovered")

    return recovered_data
