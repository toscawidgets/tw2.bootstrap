<%namespace name="tw" module="tw2.core.mako_util"/>\
<div id="${w.compound_id}" class="input-append date">\
<input ${tw.attrs(attrs=w.attrs)} value="${unicode(w.value or '')}" />\
% if not w.required:
<span class="add-on"><i class="icon-remove"></i></span>\
% endif
<span class="add-on"><i class="icon-calendar"></i></span>\
</div>