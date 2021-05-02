from flask import jsonify, abort, request, Blueprint

from wsapp.db_connection import gene_suggest

ENSEMBL_API = Blueprint('ensembl_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return ENSEMBL_API


@ENSEMBL_API.route('/gene_suggest', methods=['GET'])
def api_all():
    query_parameters = request.args
    species = query_parameters.get('species')
    query = query_parameters.get('query')
    if query_parameters.get('limit'):
        lim = query_parameters.get('limit')
        if not lim.isnumeric():
            abort(400)
    else:
        lim = None
    res = gene_suggest(species, query, lim)
    if len(res) == 0:
        abort(404)
    return jsonify({'data': res})
