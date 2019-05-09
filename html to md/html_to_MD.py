# HTML 表格
from lxml import etree
import os
# html = """
#
# <!DOCTYPE html>
# <html lang="zh-cn">
# <head>
#
# <!-- Global site tag (gtag.js) - Google Analytics -->
# <script async src="https://www.googletagmanager.com/gtag/js?id=UA-878633-1"></script>
# <script>
#   window.dataLayer = window.dataLayer || [];
#   function gtag(){dataLayer.push(arguments);}
#   gtag('js', new Date());
#
#   gtag('config', 'UA-878633-1');
# </script>
#
# <meta charset="gbk" />
# <meta name="robots" content="all" />
# <meta name="author" content="w3school.com.cn" />
# <link rel="stylesheet" type="text/css" href="/c5.css" />
# <link rel="icon" type="image/png" sizes="16x16" href="/ui2019/w3_16x16.png">
# <link rel="icon" type="image/png" sizes="32x32" href="/ui2019/w3_32x32.png">
# <link rel="icon" type="image/png" sizes="48x48" href="/ui2019/logo-48-red.png">
# <link rel="icon" type="image/png" sizes="96x96" href="/ui2019/logo-96-red.png">
# <link rel="apple-touch-icon-precomposed" sizes="180x180" href="/ui2017/logo-180.png">
#
#
# <title>HTML DOM Event 对象</title>
#
# </head>
#
# <body class="browserscripting" id="jsref">
#
# <div id="wrapper">
#
# <div id="header">
# <a href="/index.html" title="w3school 在线教程" style="float:left;">w3school 在线教程</a>
# <div id="ad_head">
# <script type="text/javascript"><!--
# google_ad_client = "pub-3381531532877742";
# /* 728x90, 创建于 08-12-1 */
# google_ad_slot = "7423315034";
# google_ad_width = 728;
# google_ad_height = 90;
# //-->
# </script>
# <script type="text/javascript"
# src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
# </script>
# </div>
# </div>
#
# <div id="navfirst">
# <ul id="menu">
# <li id="h"><a href="/h.asp" title="HTML 系列教程">HTML 系列教程</a></li>
# <li id="b"><a href="/b.asp" title="浏览器脚本教程">浏览器脚本</a></li>
# <li id="s"><a href="/s.asp" title="服务器脚本教程">服务器脚本</a></li>
# <li id="d"><a href="/d.asp" title="ASP.NET 教程">ASP.NET 教程</a></li>
# <li id="x"><a href="/x.asp" title="XML 系列教程">XML 系列教程</a></li>
# <li id="ws"><a href="/ws.asp" title="Web Services 系列教程">Web Services 系列教程</a></li>
# <li id="w"><a href="/w.asp" title="建站手册">建站手册</a></li>
# </ul>
# </div>
#
# <div id="navsecond">
#
# <div id="course"><h2>JS & DOM 参考手册</h2>
# <ul>
# <li><a href="/jsref/index.asp" title="JavaScript 和 HTML DOM 参考手册">参考手册目录</a></li>
# </ul>
# <h2>JavaScript 对象</h2>
# <ul>
# <li><a href="/jsref/jsref_obj_array.asp" title="JavaScript Array 对象参考手册">JS Array</a></li>
# <li><a href="/jsref/jsref_obj_boolean.asp" title="JavaScript Boolean 对象参考手册">JS Boolean</a></li>
# <li><a href="/jsref/jsref_obj_date.asp" title="JavaScript Date 对象参考手册">JS Date</a></li>
# <li><a href="/jsref/jsref_obj_math.asp" title="JavaScript Math 对象的参考手册">JS Math</a></li>
# <li><a href="/jsref/jsref_obj_number.asp" title="JavaScript Number 对象参考手册">JS Number</a></li>
# <li><a href="/jsref/jsref_obj_string.asp" title="JavaScript String 对象参考手册">JS String</a></li>
# <li><a href="/jsref/jsref_obj_regexp.asp" title="JavaScript RegExp 对象参考手册">JS RegExp</a></li>
# <li><a href="/jsref/jsref_obj_global.asp" title="JavaScript 全局对象参考手册">JS Functions</a></li>
# <li><a href="/jsref/jsref_events.asp" title="JavaScript 事件参考手册">JS Events</a></li>
# </ul>
# <h2>Browser 对象</h2>
# <ul>
# <li><a href="/jsref/dom_obj_window.asp" title="HTML DOM Window 对象">Window</a></li>
# <li><a href="/jsref/dom_obj_navigator.asp" title="HTML DOM Navigator 对象">Navigator</a></li>
# <li><a href="/jsref/dom_obj_screen.asp" title="HTML DOM Screen 对象">Screen</a></li>
# <li><a href="/jsref/dom_obj_history.asp" title="HTML DOM History 对象">History</a></li>
# <li><a href="/jsref/dom_obj_location.asp" title="HTML DOM Location 对象">Location</a></li>
# </ul>
# <h2>HTML DOM 对象</h2>
# <ul>
# <li><a href="/jsref/dom_obj_document.asp" title="HTML DOM Document 对象">DOM Document</a></li>
# <li><a href="/jsref/dom_obj_all.asp" title="HTML DOM Element 对象">DOM Element</a></li>
# <li><a href="/jsref/dom_obj_attributes.asp" title="HTML DOM Attribute 对象">DOM Attribute</a></li>
# <li class="currentLink"><a href="/jsref/dom_obj_event.asp" title="HTML DOM Event 对象">DOM Event</a></li>
# </ul>
# <h2>HTML 对象</h2>
# <ul>
# <li><a href="/jsref/dom_obj_anchor.asp" title="HTML DOM Anchor 对象">&lt;a&gt;</a></li>
# <li><a href="/jsref/dom_obj_area.asp" title="HTML DOM Area 对象">&lt;area&gt;</a></li>
# <li><a href="/jsref/dom_obj_audio.asp" title="HTML DOM Audio 对象">&lt;audio&gt;</a></li>
# <li><a href="/jsref/dom_obj_base.asp" title="HTML DOM Base 对象">&lt;base&gt;</a></li>
# <li><a href="/jsref/dom_obj_body.asp" title="HTML DOM Body 对象">&lt;body&gt;</a></li>
# <li><a href="/jsref/dom_obj_blockquote.asp" title="HTML DOM Blockquote 对象">&lt;blockquote&gt;</a></li>
# <li><a href="/jsref/dom_obj_pushbutton.asp" title="HTML DOM Button 对象">&lt;button&gt;</a></li>
# <li><a href="/jsref/dom_obj_canvas.asp" title="HTML DOM Canvas 对象">&lt;canvas&gt;</a></li>
# <li><a href="/jsref/dom_obj_col.asp" title="HTML DOM Column 对象">&lt;col&gt;</a></li>
# <li><a href="/jsref/dom_obj_colgroup.asp" title="HTML DOM ColumnGroup 对象">&lt;colgroup&gt;</a></li>
# <li><a href="/jsref/dom_obj_datalist.asp" title="HTML DOM Datalist 对象">&lt;datalist&gt;</a></li>
# <li><a href="/jsref/dom_obj_del.asp" title="HTML DOM Del 对象">&lt;del&gt;</a></li>
# <li><a href="/jsref/dom_obj_details.asp" title="HTML DOM Details 对象">&lt;details&gt;</a></li>
# <li><a href="/jsref/dom_obj_dialog.asp" title="HTML DOM Dialog 对象">&lt;dialog&gt;</a></li>
# <li><a href="/jsref/dom_obj_embed.asp" title="HTML DOM Embed 对象">&lt;embed&gt;</a></li>
# <li><a href="/jsref/dom_obj_fieldset.asp" title="HTML DOM Fieldset 对象">&lt;fieldset&gt;</a></li>
# <li><a href="/jsref/dom_obj_form.asp" title="HTML DOM Form 对象">&lt;form&gt;</a></li>
# <li><a href="/jsref/dom_obj_frame.asp" title="HTML DOM Frame 对象">&lt;frame&gt;</a></li>
# <li><a href="/jsref/dom_obj_frameset.asp" title="HTML DOM Frameset 对象">&lt;frameset&gt;</a></li>
# <li><a href="/jsref/dom_obj_iframe.asp" title="HTML DOM IFrame 对象">&lt;iframe&gt;</a></li>
# <li><a href="/jsref/dom_obj_image.asp" title="HTML DOM Image 对象">&lt;img&gt;</a></li>
# <li><a href="/jsref/dom_obj_ins.asp" title="HTML DOM Ins 对象">&lt;ins&gt;</a></li>
# <li><a href="/jsref/dom_obj_button.asp" title="HTML DOM Button 对象">&lt;input&gt; button</a></li>
# <li><a href="/jsref/dom_obj_checkbox.asp" title="HTML DOM Checkbox 对象">&lt;input&gt; checkbox</a></li>
# <li><a href="/jsref/dom_obj_color.asp" title="HTML DOM Color 对象">&lt;input&gt; color</a></li>
# <li><a href="/jsref/dom_obj_date.asp" title="HTML DOM Input Date 对象">&lt;input&gt; date</a></li>
# <li><a href="/jsref/dom_obj_datetime.asp" title="HTML DOM Datetime 对象">&lt;input&gt; datetime</a></li>
# <li><a href="/jsref/dom_obj_datetime-local.asp" title="HTML DOM Datetime Local 对象">&lt;input&gt; datetime-local</a></li>
# <li><a href="/jsref/dom_obj_email.asp" title="HTML DOM Email 对象">&lt;input&gt; email</a></li>
# <li><a href="/jsref/dom_obj_fileupload.asp" title="HTML DOM FileUpload 对象">&lt;input&gt; file</a></li>
# <li><a href="/jsref/dom_obj_hidden.asp" title="HTML DOM Hidden 对象">&lt;input&gt; hidden</a></li>
# <li><a href="/jsref/dom_obj_input_image.asp" title="HTML DOM Input Image 对象">&lt;input&gt; image</a></li>
# <li><a href="/jsref/dom_obj_month.asp" title="HTML DOM Month 对象">&lt;input&gt; month</a></li>
# <li><a href="/jsref/dom_obj_number.asp" title="HTML DOM Number 对象">&lt;input&gt; number</a></li>
# <li><a href="/jsref/dom_obj_password.asp" title="HTML DOM Password 对象">&lt;input&gt; password</a></li>
# <li><a href="/jsref/dom_obj_range.asp" title="HTML DOM Input Range 对象">&lt;input&gt; range</a></li>
# <li><a href="/jsref/dom_obj_radio.asp" title="HTML DOM Radio 对象">&lt;input&gt; radio</a></li>
# <li><a href="/jsref/dom_obj_reset.asp" title="HTML DOM Reset 对象">&lt;input&gt; reset</a></li>
# <li><a href="/jsref/dom_obj_search.asp" title="HTML DOM Input Search 对象">&lt;input&gt; search</a></li>
# <li><a href="/jsref/dom_obj_submit.asp" title="HTML DOM Submit 对象">&lt;input&gt; submit</a></li>
# <li><a href="/jsref/dom_obj_text.asp" title="HTML DOM Text 对象">&lt;input&gt; text</a></li>
# <li><a href="/jsref/dom_obj_input_time.asp" title="HTML DOM Input Time 对象">&lt;input&gt; time</a></li>
# <li><a href="/jsref/dom_obj_url.asp" title="HTML DOM Input URL 对象">&lt;input&gt; url</a></li>
# <li><a href="/jsref/dom_obj_week.asp" title="HTML DOM Week 对象">&lt;input&gt; week</a></li>
# <li><a href="/jsref/dom_obj_keygen.asp" title="HTML DOM Keygen 对象">&lt;keygen&gt;</a></li>
# <li><a href="/jsref/dom_obj_label.asp" title="HTML DOM Label 对象">&lt;label&gt;</a></li>
# <li><a href="/jsref/dom_obj_legend.asp" title="HTML DOM Legend 对象">&lt;legend&gt;</a></li>
# <li><a href="/jsref/dom_obj_li.asp" title="HTML DOM Li 对象">&lt;li&gt;</a></li>
# <li><a href="/jsref/dom_obj_link.asp" title="HTML DOM Link 对象">&lt;link&gt;</a></li>
# <li><a href="/jsref/dom_obj_map.asp" title="HTML DOM Map 对象">&lt;map&gt;</a></li>
# <li><a href="/jsref/dom_obj_menu.asp" title="HTML DOM Menu 对象">&lt;menu&gt;</a></li>
# <li><a href="/jsref/dom_obj_menuitem.asp" title="HTML DOM MenuItem 对象">&lt;menuitem&gt;</a></li>
# <li><a href="/jsref/dom_obj_meta.asp" title="HTML DOM Meta 对象">&lt;meta&gt;</a></li>
# <li><a href="/jsref/dom_obj_meter.asp" title="HTML DOM Meter 对象">&lt;meter&gt;</a></li>
# <li><a href="/jsref/dom_obj_object.asp" title="HTML DOM Object 对象">&lt;object&gt;</a></li>
# <li><a href="/jsref/dom_obj_ol.asp" title="HTML DOM Ol 对象">&lt;ol&gt;</a></li>
# <li><a href="/jsref/dom_obj_optgroup.asp" title="HTML DOM OptionGroup 对象">&lt;optgroup&gt;</a></li>
# <li><a href="/jsref/dom_obj_option.asp" title="HTML DOM Option 对象">&lt;option&gt;</a></li>
# <li><a href="/jsref/dom_obj_param.asp" title="HTML DOM Parameter 对象">&lt;param&gt;</a></li>
# <li><a href="/jsref/dom_obj_progress.asp" title="HTML DOM Progress 对象">&lt;progress&gt;</a></li>
# <li><a href="/jsref/dom_obj_quote.asp" title="HTML DOM Quote 对象">&lt;q&gt;</a></li>
# <li><a href="/jsref/dom_obj_script.asp" title="HTML DOM Script 对象">&lt;script&gt;</a></li>
# <li><a href="/jsref/dom_obj_select.asp" title="HTML DOM Select 对象">&lt;select&gt;</a></li>
# <li><a href="/jsref/dom_obj_source.asp" title="HTML DOM Source 对象">&lt;source&gt;</a></li>
# <li><a href="/jsref/dom_obj_style.asp" title="HTML DOM Style 对象">&lt;style&gt;</a></li>
# <li><a href="/jsref/dom_obj_table.asp" title="HTML DOM Table 对象">&lt;table&gt;</a></li>
# <li><a href="/jsref/dom_obj_tabledata.asp" title="HTML DOM TableCell 对象">&lt;td&gt;</a></li>
# <li><a href="/jsref/dom_obj_tablehead.asp" title="HTML DOM TableHeader 对象">&lt;th&gt;</a></li>
# <li><a href="/jsref/dom_obj_tablerow.asp" title="HTML DOM TableRow 对象">&lt;tr&gt;</a></li>
# <li><a href="/jsref/dom_obj_textarea.asp" title="HTML DOM Textarea 对象">&lt;textarea&gt;</a></li>
# <li><a href="/jsref/dom_obj_time.asp" title="HTML DOM Time 对象">&lt;time&gt;</a></li>
# <li><a href="/jsref/dom_obj_title.asp" title="HTML DOM Title 对象">&lt;title&gt;</a></li>
# <li><a href="/jsref/dom_obj_track.asp" title="HTML DOM Track 对象">&lt;track&gt;</a></li>
# <li><a href="/jsref/dom_obj_video.asp" title="HTML DOM Video 对象">&lt;video&gt;</a></li>
# </ul>
# </div><div id="selected">
# <h2>建站手册</h2>
# <ul>
# <li><a href="/site/index.asp" title="网站构建">网站构建</a></li>
# <li><a href="/w3c/index.asp" title="万维网联盟 (W3C)">万维网联盟 (W3C)</a></li>
# <li><a href="/browsers/index.asp" title="浏览器信息">浏览器信息</a></li>
# <li><a href="/quality/index.asp" title="网站品质">网站品质</a></li>
# <li><a href="/semweb/index.asp" title="语义网">语义网</a></li>
# <li><a href="/careers/index.asp" title="职业规划">职业规划</a></li>
# <li><a href="/hosting/index.asp" title="网站主机">网站主机</a></li>
# </ul>
#
# <h2 id="link_about"><a href="/about/index.asp" title="关于 W3School" target="_blank">关于 W3School</a></h2>
# <h2 id="link_help"><a href="/about/about_helping.asp" title="帮助 W3School" target="_blank">帮助 W3School</a></h2>
# <h2 id="link_help"><a href="/ad.html" title="W3School 广告刊例" target="_blank">广告刊例</a></h2>
#
#
# </div>
#
# </div>
#
# <div id="maincontent">
#
#
# <h1>HTML DOM Event 对象</h1>
#
#
# <div>
# <h2>实例</h2>
#
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_button">哪个鼠标按钮被点击？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_clientx">光标的坐标是？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_keycode">被按的按键的 unicode 是？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_screenxy">相对于屏幕，光标的坐标是？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_shiftkey">shift 键被按了吗？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_srcelement">哪个元素被点击了？</a></p>
# <p class="tiy"><a target="_blank" href="/tiy/t.asp?f=hdom_event_type">哪个事件类型发生了？</a></p>
# </div>
#
#
# <div>
# <h2>Event 对象</h2>
#
# <p>Event 对象代表事件的状态，比如事件在其中发生的元素、键盘按键的状态、鼠标的位置、鼠标按钮的状态。</p>
#
# <p>事件通常与函数结合使用，函数不会在事件发生前被执行！</p>
# </div>
#
#
# <div>
# <h2>事件句柄　(Event Handlers)</h2>
#
# <p>HTML 4.0 的新特性之一是能够使 HTML 事件触发浏览器中的行为，比如当用户点击某个 HTML 元素时启动一段 JavaScript。下面是一个属性列表，可将之插入 HTML 标签以定义事件的行为。</p>
#
# <table class="dataintable">
#   <tr>
#     <th style="width:30%">属性</th>
#     <th>此事件发生在何时...</th>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onabort.asp">onabort</a></td>
# 	<td>图像的加载被中断。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onblur.asp">onblur</a></td>
# 	<td>元素失去焦点。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onchange.asp">onchange</a></td>
# 	<td>域的内容被改变。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onclick.asp">onclick</a></td>
# 	<td>当用户点击某个对象时调用的事件句柄。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_ondblclick.asp">ondblclick</a></td>
# 	<td>当用户双击某个对象时调用的事件句柄。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onerror.asp">onerror</a></td>
# 	<td>在加载文档或图像时发生错误。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onfocus.asp">onfocus</a></td>
# 	<td>元素获得焦点。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onkeydown.asp">onkeydown</a></td>
# 	<td>某个键盘按键被按下。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onkeypress.asp">onkeypress</a></td>
# 	<td>某个键盘按键被按下并松开。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onkeyup.asp">onkeyup</a></td>
# 	<td>某个键盘按键被松开。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onload.asp">onload</a></td>
# 	<td>一张页面或一幅图像完成加载。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onmousedown.asp">onmousedown</a></td>
# 	<td>鼠标按钮被按下。</td>
#   </tr>
#
#   <tr>
# 	<td><a href="event_onmousemove.asp">onmousemove</a></td>
# 	<td>鼠标被移动。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onmouseout.asp">onmouseout</a></td>
# 	<td>鼠标从某元素移开。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onmouseover.asp">onmouseover</a></td>
# 	<td>鼠标移到某元素之上。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onmouseup.asp">onmouseup</a></td>
# 	<td>鼠标按键被松开。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onreset.asp">onreset</a></td>
# 	<td>重置按钮被点击。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onresize.asp">onresize</a></td>
# 	<td>窗口或框架被重新调整大小。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onselect.asp">onselect</a></td>
# 	<td>文本被选中。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onsubmit.asp">onsubmit</a></td>
# 	<td>确认按钮被点击。</td>
#   </tr>
#
#   <tr>
# 	<td><a target="_top" href="event_onunload.asp">onunload</a></td>
# 	<td>用户退出页面。</td>
#   </tr>
# </table>
# </div>
#
#
# <div>
# <h2>鼠标 / 键盘属性</h2>
#
# <table class="dataintable">
#   <tr>
#     <th style="width:30%">属性</th>
#     <th>描述</th>
#   </tr>
#   <tr>
#     <td><a href="event_altkey.asp">altKey</a></td>
#     <td>返回当事件被触发时，&quot;ALT&quot; 是否被按下。</td>
#   </tr>
#   <tr>
#     <td><a href="event_button.asp">button</a></td>
#     <td>返回当事件被触发时，哪个鼠标按钮被点击。</td>
#   </tr>
#   <tr>
#     <td><a href="event_clientx.asp">clientX</a></td>
#     <td>返回当事件被触发时，鼠标指针的水平坐标。</td>
#   </tr>
#   <tr>
#     <td><a href="event_clienty.asp">clientY</a></td>
#     <td>返回当事件被触发时，鼠标指针的垂直坐标。</td>
#   </tr>
#   <tr>
#     <td><a href="event_ctrlkey.asp">ctrlKey</a></td>
#     <td>返回当事件被触发时，&quot;CTRL&quot; 键是否被按下。</td>
#   </tr>
#   <tr>
#     <td><a href="event_metakey.asp">metaKey</a></td>
#     <td>返回当事件被触发时，&quot;meta&quot; 键是否被按下。</td>
#   </tr>
#   <tr>
#     <td><a href="event_relatedtarget.asp">relatedTarget</a></td>
#     <td>返回与事件的目标节点相关的节点。</td>
#   </tr>
#   <tr>
#     <td><a href="event_screenx.asp">screenX</a></td>
#     <td>返回当某个事件被触发时，鼠标指针的水平坐标。</td>
#   </tr>
#   <tr>
#     <td><a href="event_screeny.asp">screenY</a></td>
#     <td>返回当某个事件被触发时，鼠标指针的垂直坐标。</td>
#   </tr>
#   <tr>
#     <td><a href="event_shiftkey.asp">shiftKey</a></td>
#     <td>返回当事件被触发时，&quot;SHIFT&quot; 键是否被按下。</td>
#   </tr>
# </table>
# </div>
#
#
# <div>
# <h2>IE 属性</h2>
#
# <p>除了上面的鼠标/事件属性，IE 浏览器还支持下面的属性：</p>
#
# <table class="dataintable">
#   <tr>
#     <th style="width:30%">属性</th>
#     <th>描述</th>
#   </tr>
#   <tr>
# 		<td>cancelBubble</td>
# 		<td>如果事件句柄想阻止事件传播到包容对象，必须把该属性设为 true。</td>
#   </tr>
#   <tr>
# 		<td>fromElement</td>
# 		<td>对于 mouseover 和 mouseout 事件，fromElement 引用移出鼠标的元素。</td>
#   </tr>
#   <tr>
# 		<td>keyCode</td>
# 		<td>对于 keypress 事件，该属性声明了被敲击的键生成的 Unicode 字符码。对于 keydown 和 keyup 事件，它指定了被敲击的键的虚拟键盘码。虚拟键盘码可能和使用的键盘的布局相关。</td>
#   </tr>
#   <tr>
# 		<td>offsetX,offsetY</td>
# 		<td>发生事件的地点在事件源元素的坐标系统中的 x 坐标和 y 坐标。</td>
#   </tr>
#   <tr>
# 		<td>returnValue</td>
# 		<td>如果设置了该属性，它的值比事件句柄的返回值优先级高。把这个属性设置为 fasle，可以取消发生事件的源元素的默认动作。</td>
#   </tr>
#   <tr>
# 		<td>srcElement</td>
# 		<td>对于生成事件的 Window 对象、Document 对象或 Element 对象的引用。</td>
#   </tr>
#   <tr>
# 		<td>toElement</td>
# 		<td>对于 mouseover 和 mouseout 事件，该属性引用移入鼠标的元素。</td>
#   </tr>
#   <tr>
# 		<td>x,y</td>
# 		<td>事件发生的位置的 x 坐标和 y 坐标，它们相对于用CSS动态定位的最内层包容元素。</td>
#   </tr>
# </table>
# </div>
#
#
# <div>
# <h2>标准 Event 属性</h2>
#
# <p>下面列出了 2 级 DOM 事件标准定义的属性。</p>
#
# <table class="dataintable">
#   <tr>
#     <th style="width:30%">属性</th>
#     <th>描述</th>
#   </tr>
#   <tr>
#     <td><a href="event_bubbles.asp">bubbles</a></td>
#     <td>返回布尔值，指示事件是否是起泡事件类型。</td>
#   </tr>
#   <tr>
#     <td><a href="event_cancelable.asp">cancelable</a></td>
#     <td>返回布尔值，指示事件是否可拥可取消的默认动作。</td>
#   </tr>
#   <tr>
#     <td><a href="event_currenttarget.asp">currentTarget</a></td>
#     <td>返回其事件监听器触发该事件的元素。</td>
#   </tr>
#   <tr>
#     <td><a href="event_eventphase.asp">eventPhase</a></td>
#     <td>返回事件传播的当前阶段。</td>
#   </tr>
#   <tr>
#     <td><a href="event_target.asp">target</a></td>
#     <td>返回触发此事件的元素（事件的目标节点）。</td>
#   </tr>
#   <tr>
#     <td><a href="event_timestamp.asp">timeStamp</a></td>
#     <td>返回事件生成的日期和时间。</td>
#   </tr>
#   <tr>
#     <td><a href="event_type.asp">type</a></td>
#     <td>返回当前 Event 对象表示的事件的名称。</td>
#   </tr>
# </table>
# </div>
#
#
# <div>
# <h2>标准 Event 方法</h2>
#
# <p>下面列出了 2 级 DOM 事件标准定义的方法。IE 的事件模型不支持这些方法：</p>
#
# <table class="dataintable">
#   <tr>
#     <th style="width:30%">方法</th>
#     <th>描述</th>
#   </tr>
#   <tr>
#     <td><a href="event_initevent.asp">initEvent()</a></td>
#     <td>初始化新创建的 Event 对象的属性。</td>
#   </tr>
#   <tr>
#     <td><a href="event_preventdefault.asp">preventDefault()</a></td>
#     <td>通知浏览器不要执行与事件关联的默认动作。</td>
#   </tr>
#   <tr>
#     <td class="no_wrap"><a href="event_stoppropagation.asp">stopPropagation()</a></td>
#     <td>不再派发事件。</td>
#   </tr>
# </table>
# </div>
#
#
# <div style="background-color:#fcfdf8; padding:0;">
# <script async src="//pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"></script>
# <!-- W3School 正文底部广告位 -->
# <ins class="adsbygoogle"
#      style="display:inline-block;width:800px;height:250px"
#      data-ad-client="ca-pub-3381531532877742"
#      data-ad-slot="9384069314"></ins>
# <script>
# (adsbygoogle = window.adsbygoogle || []).push({});
# </script>
# </div>
#
# </div>
# <!-- maincontent end -->
#
# <div id="sidebar">
#
# <div id="tools">
# <h5 id="tools_reference"><a href="/jsref/index.asp">JavaScript 参考手册</a></h5>
# <h5 id="tools_example"><a href="/example/jseg_examples.asp">JavaScript 实例</a></h5>
# <h5 id="tools_quiz"><a href="/js/js_quiz.asp">JavaScript 测验</a></h5>
# </div>
#
# <div id="ad">
# <script type="text/javascript"><!--
# google_ad_client = "ca-pub-3381531532877742";
# /* sidebar-160x600 */
# google_ad_slot = "3772569310";
# google_ad_width = 160;
# google_ad_height = 600;
# //-->
# </script>
# <script type="text/javascript"
# src="http://pagead2.googlesyndication.com/pagead/show_ads.js">
# </script>
# </div>
#
# </div>
#
# <div id="footer">
# <p id="p1">
# W3School 简体中文版提供的内容仅用于培训和测试，不保证内容的正确性。通过使用本站内容随之而来的风险与本站无关。
# </p>
#
# <p id="p2">
# 使用条款和隐私条款。版权所有，保留一切权利。
# 赞助商：<a href="http://www.ykinvestment.com/">上海赢科投资有限公司</a>。
# <a target="_blank" href="http://www.miitbeian.gov.cn/">蒙ICP备06004630号</a>
# <a style="color: #000; margin-left: 20px;" href="/ad.html" target="_blank" title="W3School 广告刊例">广告刊例</a>
# </p>
# </div>
#
#
# </div>
# <!-- wrapper end -->
#
# </body>
#
# </html>"""

class HtmlToMd:
    """
    1. 找tbody,需要考虑多个tbody的情况
    2. 找th 可能存在a等子元素，需要遍历出来,递归，直到找到text()
    3. 找td 同样存在子元素
    """
    def __init__(self,html):
        self._tree = etree.HTML(str(html))
        try:
            self.tbodys = self._tree.xpath("//tbody")
            if len(self.tbodys) == 0:
                self.tbodys = self._tree.xpath("//table")
        except TypeError:
            print("未找到html表格，请检查格式是否正确")
            os._exit(1)

    def __getchild(self,father_node):
        child_nodes = father_node.xpath('child::*')
        # 没有子节点，返回他的文本对象，作为递归的出口
        if len(child_nodes) == 0:
            text_list = father_node.xpath("./text()")
            # 考虑多个并列文本节点的情况
            for text in text_list:
                print(text, end=" ")
        else:
            for child_node in child_nodes:
                self.__getchild(child_node)

    def __getinfo(self,tbody):
        # 寻找tr,th,默认第一个tr保存表头信息，不标准的将会被忽略
        trlist = tbody.xpath("./tr")
        ths = trlist[0].xpath("./th")
        num =len(ths)
        # 将表头弹出列表
        trlist.pop(0)
        # 寻找表头文本节点
        for th in ths:
            print("|", end="")
            self.__getchild(th)
        print("|\n|",end="")

        for i in range(num):
            print("---|",end = "")
        print("\n",end="")
        for tr in trlist:
            tds =tr.xpath("./td")
            for td in tds:
                print("|", end="")
                self.__getchild(td)
            print("|")

    def run(self):
        for tbody in self.tbodys:
            self.__getinfo(tbody)
            print("\n")

if __name__ == '__main__':
    with open("test.html","r") as fp:
        html = fp.read()
    print(type(html))
    htm = HtmlToMd(html)
    htm.run()

