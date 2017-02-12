# -*- coding: utf-8 -*-

from deform import Form, ValidationFailure
from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource
from js.bootstrap_daterangepicker import daterangepicker
from js.jquery import jquery
from js.jquery_form import jquery_form
from js.jquery_maskedinput import jquery_maskedinput
from js.jquery_maskmoney import jquery_maskmoney
from js.jquery_sortable import jquery_sortable
from js.jquery_timepicker_addon import timepicker
from js.jqueryui import ui_autocomplete
from js.jqueryui import ui_datepicker
from js.jqueryui import ui_sortable
from js.modernizr import modernizr
from js.select2 import select2
from js.tinymce import tinymce
from pkg_resources import resource_filename


deform_dir = resource_filename(
    "deform",
    "static")
library = Library(
    "deform",
    deform_dir)

deform_js = Resource(
    library,
    "scripts/deform.js",
    depends=[jquery, ])

deform_form_css = Resource(
    library,
    "css/form.css")
deform_beautify_css = Resource(
    library,
    "css/beautify.css")

deform_css = Group([deform_form_css, deform_beautify_css, ])

deform_basic = Group([deform_form_css, deform_js, ])
deform = Group([deform_css, deform_js, ])

modernizr = Resource(
    library,
    'scripts/modernizr.custom.input-types-and-atts.js')

typeahead_js = Resource(
    library,
    'scripts/typeahead.min.js',
    depends=[jquery, ])
typeahead_css = Resource(
    library,
    'css/typeahead.css')
typeahead = Group([typeahead_js, typeahead_css])

fileupload = Resource(
    library,
    'scripts/file_upload.js')

pickadate_js_legacy = Resource(
    library,
    'pickadate/legacy.js')
pickadate_js_base = Resource(
    library,
    'pickadate/picker.js',
    depends=[pickadate_js_legacy, ])
pickadate_js_date = Resource(
    library,
    'pickadate/picker.date.js',
    depends=[pickadate_js_base, ])
pickadate_js_time = Resource(
    library,
    'pickadate/picker.time.js',
    depends=[pickadate_js_base, ])
pickadate_js = Group([
    pickadate_js_date,
    pickadate_js_time, ])
pickadate_css_base = Resource(
    library,
    'pickadate/themes/default.css')
pickadate_css_date = Resource(
    library,
    'pickadate/themes/default.date.css',
    depends=[pickadate_css_base, ])
pickadate_css_time = Resource(
    library,
    'pickadate/themes/default.time.css',
    depends=[pickadate_css_base, ])
pickadate_css = Group([
    pickadate_css_date,
    pickadate_css_time, ])

pickadate = Group([pickadate_js, pickadate_css, ])

pickadate_ar = Resource(
    library,
    'pickadate/translations/ar.js',
    depends=[pickadate])

pickadate_bg = Resource(
    library,
    'pickadate/translations/bg_BG.js',
    depends=[pickadate])

pickadate_bs_BA = Resource(
    library,
    'pickadate/translations/bs_BA.js',
    depends=[pickadate])

pickadate_ca_ES = Resource(
    library,
    'pickadate/translations/ca_ES.js',
    depends=[pickadate])

pickadate_cs_CZ = Resource(
    library,
    'pickadate/translations/cs_CZ.js',
    depends=[pickadate])

pickadate_da_DK = Resource(
    library,
    'pickadate/translations/da_DK.js',
    depends=[pickadate])

pickadate_de = Resource(
    library,
    'pickadate/translations/de_DE.js',
    depends=[pickadate])

pickadate_el_GR = Resource(
    library,
    'pickadate/translations/el_GR.js',
    depends=[pickadate])

pickadate_es = Resource(
    library,
    'pickadate/translations/es_ES.js',
    depends=[pickadate])

pickadate_et_EE = Resource(
    library,
    'pickadate/translations/et_EE.js',
    depends=[pickadate])

pickadate_eu_ES = Resource(
    library,
    'pickadate/translations/eu_ES.js',
    depends=[pickadate])

pickadate_fa_ir = Resource(
    library,
    'pickadate/translations/fa_ir.js',
    depends=[pickadate])

pickadate_fi = Resource(
    library,
    'pickadate/translations/fi_FI.js',
    depends=[pickadate])

pickadate_fr = Resource(
    library,
    'pickadate/translations/fr_FR.js',
    depends=[pickadate])

pickadate_gl_ES = Resource(
    library,
    'pickadate/translations/gl_ES.js',
    depends=[pickadate])

pickadate_he_IL = Resource(
    library,
    'pickadate/translations/he_IL.js',
    depends=[pickadate])

pickadate_hi_IN = Resource(
    library,
    'pickadate/translations/hi_IN.js',
    depends=[pickadate])

pickadate_hr = Resource(
    library,
    'pickadate/translations/hr_HR.js',
    depends=[pickadate])

pickadate_hu = Resource(
    library,
    'pickadate/translations/hu_HU.js',
    depends=[pickadate])

pickadate_id = Resource(
    library,
    'pickadate/translations/id_ID.js',
    depends=[pickadate])

pickadate_is = Resource(
    library,
    'pickadate/translations/is_IS.js',
    depends=[pickadate])

pickadate_it = Resource(
    library,
    'pickadate/translations/it_IT.js',
    depends=[pickadate])

pickadate_ja_JP = Resource(
    library,
    'pickadate/translations/ja_JP.js',
    depends=[pickadate])

pickadate_ko_KR = Resource(
    library,
    'pickadate/translations/ko_KR.js',
    depends=[pickadate])

pickadate_lt = Resource(
    library,
    'pickadate/translations/lt_LT.js',
    depends=[pickadate])

pickadate_lv = Resource(
    library,
    'pickadate/translations/lv_LV.js',
    depends=[pickadate])

pickadate_nb_NO = Resource(
    library,
    'pickadate/translations/nb_NO.js',
    depends=[pickadate])

pickadate_ne_NP = Resource(
    library,
    'pickadate/translations/ne_NP.js',
    depends=[pickadate])

pickadate_nl = Resource(
    library,
    'pickadate/translations/nl_NL.js',
    depends=[pickadate])

pickadate_pl = Resource(
    library,
    'pickadate/translations/pl_PL.js',
    depends=[pickadate])

pickadate_pt_BR = Resource(
    library,
    'pickadate/translations/pt_BR.js',
    depends=[pickadate])

pickadate_pt = Resource(
    library,
    'pickadate/translations/pt_PT.js',
    depends=[pickadate])

pickadate_ro = Resource(
    library,
    'pickadate/translations/ro_RO.js',
    depends=[pickadate])

pickadate_ru = Resource(
    library,
    'pickadate/translations/ru_RU.js',
    depends=[pickadate])

pickadate_sl_SI = Resource(
    library,
    'pickadate/translations/sl_SI.js',
    depends=[pickadate])

pickadate_sv_SE = Resource(
    library,
    'pickadate/translations/sv_SE.js',
    depends=[pickadate])

pickadate_th = Resource(
    library,
    'pickadate/translations/th_TH.js',
    depends=[pickadate])

pickadate_tr = Resource(
    library,
    'pickadate/translations/tr_TR.js',
    depends=[pickadate])

pickadate_uk_UA = Resource(
    library,
    'pickadate/translations/uk_UA.js',
    depends=[pickadate])

pickadate_vi_VN = Resource(
    library,
    'pickadate/translations/vi_VN.js',
    depends=[pickadate])

pickadate_zh_CN = Resource(
    library,
    'pickadate/translations/zh_CN.js',
    depends=[pickadate])

pickadate_zh_TW = Resource(
    library,
    'pickadate/translations/zh_TW.js',
    depends=[pickadate])

pickadate_locales = {
    'pickadate_ar': [pickadate_ar, ],
    'pickadate_bg': [pickadate_bg, ],
    'pickadate_bs_BA': [pickadate_bs_BA, ],
    'pickadate_ca_ES': [pickadate_ca_ES, ],
    'pickadate_cs_CZ': [pickadate_cs_CZ, ],
    'pickadate_da_DK': [pickadate_da_DK, ],
    'pickadate_de': [pickadate_de, ],
    'pickadate_el_GR': [pickadate_el_GR, ],
    'pickadate_es': [pickadate_es, ],
    'pickadate_en': pickadate_js,
    'pickadate_et_EE': [pickadate_et_EE, ],
    'pickadate_eu_ES': [pickadate_eu_ES, ],
    'pickadate_fa_ir': [pickadate_fa_ir, ],
    'pickadate_fi': [pickadate_fi, ],
    'pickadate_fr': [pickadate_fr, ],
    'pickadate_gl_ES': [pickadate_gl_ES, ],
    'pickadate_he_IL': [pickadate_he_IL, ],
    'pickadate_hi_IN': [pickadate_hi_IN, ],
    'pickadate_hr': [pickadate_hr, ],
    'pickadate_hu': [pickadate_hu, ],
    'pickadate_id': [pickadate_id, ],
    'pickadate_is': [pickadate_is, ],
    'pickadate_it': [pickadate_it, ],
    'pickadate_ja_JP': [pickadate_ja_JP, ],
    'pickadate_ko_KR': [pickadate_ko_KR, ],
    'pickadate_lt': [pickadate_lt, ],
    'pickadate_lv': [pickadate_lv, ],
    'pickadate_nb_NO': [pickadate_nb_NO, ],
    'pickadate_ne_NP': [pickadate_ne_NP, ],
    'pickadate_nl': [pickadate_nl, ],
    'pickadate_pl': [pickadate_pl, ],
    'pickadate_pt_BR': [pickadate_pt_BR, ],
    'pickadate_pt': [pickadate_pt, ],
    'pickadate_ro': [pickadate_ro, ],
    'pickadate_ru': [pickadate_ru, ],
    'pickadate_sl_SI': [pickadate_sl_SI, ],
    'pickadate_sv_SE': [pickadate_sv_SE, ],
    'pickadate_th': [pickadate_th, ],
    'pickadate_tr': [pickadate_tr, ],
    'pickadate_uk_UA': [pickadate_uk_UA, ],
    'pickadate_vi_VN': [pickadate_vi_VN, ],
    'pickadate_zh_CN': [pickadate_zh_CN, ],
    'pickadate_zh_TW': [pickadate_zh_TW, ],
}

resource_mapping = {
    'datetimepicker': [timepicker, ],
    'deform': [deform_js, ],
    'fileupload': [fileupload, ],
    'jquery': [jquery, ],
    'jquery.form': [jquery_form, ],
    'jquery.maskMoney': [jquery_maskmoney, ],
    'jquery.maskedinput': [jquery_maskedinput, ],
    'jqueryui': [ui_autocomplete, ui_datepicker, ui_sortable, ],
    'modernizr': [modernizr, ],
    'daterangepicker': [daterangepicker, ],
    'pickadate': [pickadate, ],
    'select2': [select2, ],
    'sortable': [jquery_sortable, ],
    'tinymce': [tinymce, ],
    'typeahead': [typeahead, ],
}


def auto_need(form):
    """Automatically ``need()`` the relevant Fanstatic resources for a form.

    This function automatically utilises libraries in the ``js.*`` namespace
    (such as ``js.jquery``, ``js.tinymce`` and so forth) to allow Fanstatic
    to better manage these resources (caching, minifications) and avoid
    duplication across the rest of your application.
    """

    requirements = form.get_widget_requirements()

    for library, version in requirements:
        resources = resource_mapping[library]
        if not isinstance(resources, list):  # pragma: no cover (bw compat only)
            resources = [resources]
        for resource in resources:
            resource.need()

    if form.use_ajax:
        jquery_form.need()


def set_pickadate_locales():
    from deform import widget
    for key, value in pickadate_locales.items():
        resource_mapping[key] = value
        rendered = None
        if isinstance(value, list):
            rendered = value[0].render('deform:static')
        elif isinstance(value, Group):
            rendered = []
            for assest in value.list_assets():
                rendered.append(assest.render('deform:static'))
        else:
            rendered = value
        widget.default_resource_registry.set_js_resources(key, None, rendered)


def includeme(config=None):

    _marker = object()

    def form_render(self, appstruct=_marker, **kw):

        if appstruct is not _marker:  # pragma: no cover  (copied from deform)
            kw['appstruct'] = appstruct

        html = super(Form, self).render(**kw)
        auto_need(self)

        return html

    def validationfailure_render(self):

        auto_need(self.field)

        return self.field.widget.serialize(self.field, self.cstruct)

    def patch_deform():

        Form.render = form_render
        ValidationFailure.render = validationfailure_render
        set_pickadate_locales()

    patch_deform()
