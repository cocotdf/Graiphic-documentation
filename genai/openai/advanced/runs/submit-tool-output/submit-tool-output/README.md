<h1>Submit Tool Output</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/submit-tool-output.png" alt="Submit Tool Output" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="/_assets/shared-images/77/7741fcb2046c-copenailvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="request" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>request : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="tool_outputs (required)" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="42"/></td>
      <td valign="top"><strong>tool_outputs (required) : <em>array of cluster</em></strong>
<ul>
  <li><img alt="tool_call_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>tool_call_id : <em>string</em></strong></li>
  <li><img alt="output" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>output : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="stream (optional)" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>stream (optional) : <em>boolean</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="request" src="assets/request.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="run_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>run_id : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI out" src="/_assets/shared-images/80/80afcce65438-iopenailvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="response" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>response : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="object" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>object : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="created_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>created_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="assistant_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>assistant_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="status" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>status : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="required_action" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>required_action : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="submit_tool_outputs" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>submit_tool_outputs : <em>cluster</em></strong>
<ul>
  <li><img alt="tool_calls" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>tool_calls : <em>array of cluster</em></strong>
<ul>
  <li><img alt="id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>id : <em>string</em></strong></li>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="function" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>function : <em>cluster</em></strong>
<ul>
  <li><img alt="name" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>name : <em>string</em></strong></li>
  <li><img alt="arguments" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>arguments : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="last_error" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>last_error : <em>cluster</em></strong>
<ul>
  <li><img alt="code" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>code : <em>string</em></strong></li>
  <li><img alt="message" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>message : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>expires_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="started_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>started_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="cancelled_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>cancelled_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="failed_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>failed_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="completed_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>completed_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="incomplete_details" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="reason" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>reason : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="model" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>model : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="instructions" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>instructions : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tools" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tools : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="usage" src="/_assets/shared-images/b0/b0472b1126d2-inclst.png" width="42"/></td>
      <td valign="top"><strong>usage : <em>cluster</em></strong>
<ul>
  <li><img alt="completion_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>completion_tokens : <em>integer</em></strong></li>
  <li><img alt="prompt_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>prompt_tokens : <em>integer</em></strong></li>
  <li><img alt="total_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>total_tokens : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="temperature" src="/_assets/shared-images/17/17a2527061b3-idbl.png" width="42"/></td>
      <td valign="top"><strong>temperature : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_p" src="/_assets/shared-images/17/17a2527061b3-idbl.png" width="42"/></td>
      <td valign="top"><strong>top_p : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_prompt_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>max_prompt_tokens : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_completion_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>max_completion_tokens : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="truncation_strategy" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>truncation_strategy : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="last_messages" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>last_messages : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_choice" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_choice : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="parallel_tool_calls" src="/_assets/shared-images/e7/e72f669fda50-ibool.png" width="42"/></td>
      <td valign="top"><strong>parallel_tool_calls : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="response_format" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>response_format : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="/_assets/shared-images/c5/c5b6595ed048-response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
