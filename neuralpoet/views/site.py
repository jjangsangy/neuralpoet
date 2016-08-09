from flask import Blueprint, render_template

from ..forms import LinkForm

site = Blueprint('site', __name__)


@site.route('/', methods=['GET', 'POST'])
def index():
    form = LinkForm()
    return render_template('index.html', form=form)
