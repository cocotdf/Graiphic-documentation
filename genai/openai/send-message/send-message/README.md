<h1>Send Message</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/send-message.png" alt="Send Message" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Assistants in" src="/_assets/shared-images/77/7741fcb2046c-copenailvclass.png" width="42"/></td>
      <td valign="top"><strong>Assistants in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="message_parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>message_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="role (required)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>role (required) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="content (required)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>content (required) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="attachments (optional)" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="42"/></td>
      <td valign="top"><strong>attachments (optional) : <em>array of cluster</em></strong>
<ul>
  <li><img alt="file_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>file_id : <em>string</em></strong></li>
  <li><img alt="tools" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="32"/> <strong>tools : <em>array of cluster</em></strong>
<ul>
  <li><img alt="incomplete_details" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>type : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata (optional) : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="message_parameters" src="/_assets/shared-images/d7/d797fb720739-request.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="run_parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>run_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="assistant_id (required)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>assistant_id (required) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="model (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>model (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="instructions (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>instructions (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="additional_instructions (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>additional_instructions (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="additional_messages (optional)" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="42"/></td>
      <td valign="top"><strong>additional_messages (optional) : <em>array of cluster</em></strong>
<ul>
  <li><img alt="role" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>role : <em>string</em></strong></li>
  <li><img alt="content" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="32"/> <strong>content : <em>class</em></strong></li>
  <li><img alt="attachments" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="32"/> <strong>attachments : <em>array of cluster</em></strong>
<ul>
  <li><img alt="file_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>file_id : <em>string</em></strong></li>
  <li><img alt="tools" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="32"/> <strong>tools : <em>array of cluster</em></strong>
<ul>
  <li><img alt="incomplete_details" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>type : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></li>
  <li><img alt="metadata" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="32"/> <strong>metadata : <em>class</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tools (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tools (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="temperature (optional)" src="/_assets/shared-images/c7/c71945e6f909-cdbl.png" width="42"/></td>
      <td valign="top"><strong>temperature (optional) : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_p (optional)" src="/_assets/shared-images/c7/c71945e6f909-cdbl.png" width="42"/></td>
      <td valign="top"><strong>top_p (optional) : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="stream (optional)" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>stream (optional) : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_prompt_tokens (optional)" src="/_assets/shared-images/4b/4b060a6ee305-cu32.png" width="42"/></td>
      <td valign="top"><strong>max_prompt_tokens (optional) : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_completion_tokens (optional)" src="/_assets/shared-images/4b/4b060a6ee305-cu32.png" width="42"/></td>
      <td valign="top"><strong>max_completion_tokens (optional) : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="truncation_strategy (optional)" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="42"/></td>
      <td valign="top"><strong>truncation_strategy (optional) : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="last_messages" src="/_assets/shared-images/c7/c71945e6f909-cdbl.png" width="32"/> <strong>last_messages : <em>float</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_choice (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_choice (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="parallel_tool_calls (optional)" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>parallel_tool_calls (optional) : <em>boolean</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="run_parameters" src="/_assets/shared-images/99/99f1006f2eb4-request.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Assistants out" src="/_assets/shared-images/80/80afcce65438-iopenailvclass.png" width="42"/></td>
      <td valign="top"><strong>Assistants out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
