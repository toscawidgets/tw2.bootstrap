<%namespace name="tw" module="tw2.core.mako_util"/>
% for c in w.children_hidden:
  ${c.display() | n}
% endfor
% for i, c in enumerate(w.children_non_hidden):
  <div \
    class="control-group ${(getattr(c, 'required', False) and ' required' or '') + (c.error_msg and ' error' or '')}" \
    % if w.hover_help and c.help_text:
      title="${c.help_text}" \
    % endif
    ${tw.attrs(attrs=c.container_attrs)} \
    id="${c.compound_id or ''}:container">
    <label class="control-label" for="${c.compound_id or ''}">${c.label or ''}</label>
    <div class="controls">
      ${c.display() | n}
      % if c.error_msg:
        <span id="${c.compound_id or ''}:error" class="error help-inline">${c.error_msg or ''}</span>
      % endif
      % if not w.hover_help and c.help_text:
        <p class="help-block">${c.help_text or ''}</p>
      % endif
    </div>
  </div>
% endfor
% if w.rollup_errors:
  <div class="control-group error">
    <div id="${w.compound_id or ''}:error" class="controls error">
      % for error in w.rollup_errors:
        <p class="help-block">${error}</p>
      % endfor
    </div>
  </div>
% endif
