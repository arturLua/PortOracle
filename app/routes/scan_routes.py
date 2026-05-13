from flask import Blueprint, jsonify, request
from app.utils.network import resolve_hostname
from app.services.scanner import run_scan
from app.config import DEFAULT_END_PORT, DEFAULT_START_PORT, DEFAULT_TIMEOUT

scan_bp = Blueprint('scan', __name__)

@scan_bp.route('/scan/<target>', methods=['GET'])
def scan(target):
    try:
        ip = resolve_hostname(target)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

    start = request.args.get('start', default=DEFAULT_START_PORT, type=int)
    end = request.args.get('end', default=DEFAULT_END_PORT, type=int)
    timeout = request.args.get('timeout', default=DEFAULT_TIMEOUT, type=float)

    results = run_scan(ip, start, end, timeout)
    return jsonify(results)