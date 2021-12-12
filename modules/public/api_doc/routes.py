# Import flask dependencies
from flask import Blueprint, redirect, url_for

mod_doc = Blueprint('', __name__, url_prefix='')


class ViewDoc(object):
    """
    """
    def __init__(self):
        super().__init__()

    @mod_doc.route('/', methods=['GET'])
    def home():
        return redirect("/docs/")
