from flask import jsonify, abort, request, Blueprint

from wsapp.db_connection import gene_suggest,species_suggest

ENSEMBL_API = Blueprint('ensembl_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return ENSEMBL_API


@ENSEMBL_API.route('/gene_suggest', methods=['GET'])
def api_all():
    query_parameters = request.args
    species = query_parameters.get('species')
    query = query_parameters.get('query')
    lim = query_parameters.get('limit')

    if species == None or query == None:
        abort(400)

    if lim != None and not lim.isnumeric():
            abort(400)

    res = gene_suggest(species, query, lim)
    if len(res) == 0:
        abort(404)
    return jsonify({'data': res})

@ENSEMBL_API.route('/species_suggest', methods=['GET'])
def species_auto():
    query_parameters = request.args
    query = query_parameters.get('query')
    lim = query_parameters.get('limit')

    if query == None:
        abort(400)

    if lim != None and not lim.isnumeric():
        abort(400)

    res = species_suggest( query, lim)
    if len(res) == 0:
        abort(404)
    return jsonify({'data': res})