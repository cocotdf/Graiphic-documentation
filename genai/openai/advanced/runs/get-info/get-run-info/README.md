<h1>Get Run Info</h1>

<h2>Description</h2>

<p>Retrieves a run. Type : VI.</p>

<p align="center"><img src="assets/get-run-info.png" alt="Get Run Info" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="assets/cOpenAIlvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="run_id" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>run_id : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI out" src="assets/iOpenAIlvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="response" src="assets/icclst.png" width="32"/> <strong>response : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="id" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="object" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>object : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="created_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>created_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="assistant_id" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>assistant_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="status" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>status : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="required_action" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>required_action : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="assets/istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="submit_tool_outputs" src="assets/icclst.png" width="32"/> <strong>submit_tool_outputs : <em>cluster</em></strong>
<ul>
  <li><img alt="tool_calls" src="assets/i1dcclst.png" width="32"/> <strong>tool_calls : <em>array of cluster</em></strong>
<ul>
  <li><img alt="id" src="assets/istr.png" width="32"/> <strong>id : <em>string</em></strong></li>
  <li><img alt="type" src="assets/istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="function" src="assets/icclst.png" width="32"/> <strong>function : <em>cluster</em></strong>
<ul>
  <li><img alt="name" src="assets/istr.png" width="32"/> <strong>name : <em>string</em></strong></li>
  <li><img alt="arguments" src="assets/istr.png" width="32"/> <strong>arguments : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="last_error" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>last_error : <em>cluster</em></strong>
<ul>
  <li><img alt="code" src="assets/istr.png" width="32"/> <strong>code : <em>string</em></strong></li>
  <li><img alt="message" src="assets/istr.png" width="32"/> <strong>message : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>expires_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="started_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>started_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="cancelled_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>cancelled_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="failed_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>failed_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="completed_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>completed_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="incomplete_details" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="reason" src="assets/istr.png" width="32"/> <strong>reason : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="model" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>model : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="instructions" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>instructions : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tools" src="assets/itoolslvclass.png" width="42"/></td>
      <td valign="top"><strong>tools : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata" src="assets/imetadatalvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="usage" src="assets/inclst.png" width="42"/></td>
      <td valign="top"><strong>usage : <em>cluster</em></strong>
<ul>
  <li><img alt="completion_tokens" src="assets/iu32.png" width="32"/> <strong>completion_tokens : <em>integer</em></strong></li>
  <li><img alt="prompt_tokens" src="assets/iu32.png" width="32"/> <strong>prompt_tokens : <em>integer</em></strong></li>
  <li><img alt="total_tokens" src="assets/iu32.png" width="32"/> <strong>total_tokens : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="temperature" src="assets/idbl.png" width="42"/></td>
      <td valign="top"><strong>temperature : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_p" src="assets/idbl.png" width="42"/></td>
      <td valign="top"><strong>top_p : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_prompt_tokens" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>max_prompt_tokens : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="max_completion_tokens" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>max_completion_tokens : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="truncation_strategy" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>truncation_strategy : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="assets/istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="last_messages" src="assets/iu32.png" width="32"/> <strong>last_messages : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_choice" src="assets/itool__choicelvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_choice : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="parallel_tool_calls" src="assets/ibool.png" width="42"/></td>
      <td valign="top"><strong>parallel_tool_calls : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="response_format" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>response_format : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="assets/response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
