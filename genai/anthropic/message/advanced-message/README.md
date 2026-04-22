<h1>Advanced Message</h1>

<h2>Description</h2>

<p>Send a structured list of input messages with text and/or image content, and the model will generate the next message in the conversation. The Messages API can be used for either single queries or stateless multi-turn conversations. Type : VI.</p>

<p align="center"><img src="assets/advanced-message.png" alt="Advanced Message" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Anthropic in" src="/_assets/shared-images/82/8241d0fa280e-canthropiclvclass.png" width="42"/></td>
      <td valign="top"><strong>Anthropic in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="json_request" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>json_request : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Anthropic out" src="/_assets/shared-images/f4/f47f1679d4c8-ianthropiclvclass.png" width="42"/></td>
      <td valign="top"><strong>Anthropic out : <em>class</em></strong></td>
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
      <td width="64" valign="top"><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>type : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="role" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>role : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="model" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>model : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="content" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="42"/></td>
      <td valign="top"><strong>content : <em>array of cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
  <li><img alt="text" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>text : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="stop_reason" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>stop_reason : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="stop_sequence" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>stop_sequence : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="usage" src="/_assets/shared-images/b0/b0472b1126d2-inclst.png" width="42"/></td>
      <td valign="top"><strong>usage : <em>cluster</em></strong>
<ul>
  <li><img alt="input_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>input_tokens : <em>integer</em></strong></li>
  <li><img alt="cache_creation_input_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>cache_creation_input_tokens : <em>integer</em></strong></li>
  <li><img alt="cache_read_input_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>cache_read_input_tokens : <em>integer</em></strong></li>
  <li><img alt="output_tokens" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>output_tokens : <em>integer</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="/_assets/shared-images/2d/2dfb581d8db9-response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="last_response" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>last_response : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>
