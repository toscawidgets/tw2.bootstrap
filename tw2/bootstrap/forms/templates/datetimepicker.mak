<%namespace name="tw" module="tw2.core.mako_util"/>\
<div id="${w.compound_id}" class="input-append date">\
<input ${tw.attrs(attrs=dict((k, w.attrs[k]) for k in w.attrs if k != 'id' and k != 'value' ))} \
value="${w.value or ''}" data-date="${w.value or ''}" data-date-format="${w.format}"/>\
% if not w.required:
<span class="add-on"><i class="icon-remove"></i></span>\
% endif
<span class="add-on"><i class="icon-calendar"></i></span>\
</div>
