<%namespace name="tw" module="tw2.core.mako_util"/>\
<ul ${tw.attrs(attrs=w.attrs)}>
   % for group, opts in w.grouped_options:
   % if group:
    <li>
    <div class="group_header">${group}</div>
    <ul>
   % endif   
   % for attrs, desc in opts:
    <li>
        <label class="${attrs['type']}" for="${attrs['id']}">
        <input ${tw.attrs(attrs=attrs)}>
        ${desc}</label>
    </li>
   % endfor
   % if group:
    </li>
    </ul>
   % endif   
   % endfor
</ul>
