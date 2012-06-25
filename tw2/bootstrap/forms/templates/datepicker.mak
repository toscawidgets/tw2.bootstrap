<%namespace name="tw" module="tw2.core.mako_util"/>\
% if w.style == 'component':
  <div class="input-append date" id="${w.compound_id}" data-date="${w.value or ''}" data-date-format="${w.format}">
    <input ${tw.attrs(attrs=dict((k, w.attrs[k]) for k in w.attrs if k != 'id' and k != 'value' ))} value="${w.value or ''}" />
    <span class="add-on"><i class="icon-th"></i></span>
  </div>
% else:
  <input ${tw.attrs(attrs=dict((k, w.attrs[k]) for k in w.attrs if k != 'value'))} value="${w.value or ''}" data-date="${w.value or ''}" data-date-format="${w.format}" />
% endif