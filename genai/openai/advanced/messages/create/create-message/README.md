<h1>Create Message</h1>

<h2>Description</h2>

<p>Create a message. Type : VI.</p>

<p align="center"><img src="assets/create-message.png" alt="Create Message" width="270" /></p>

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
      <td valign="top" width="30%"><p align="center"><img alt="request" src="/_assets/shared-images/d7/d797fb720739-request.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
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
      <td width="64" valign="top"><img alt="status" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>status : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="incomplete_details" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="reason" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>reason : <em>string</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="completed_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>completed_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="incomplete_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>incomplete_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="role" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>role : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="content" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>content : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="assistant_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>assistant_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="run_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>run_id : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="attachments" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="42"/></td>
      <td valign="top"><strong>attachments : <em>array of cluster</em></strong>
<ul>
  <li><img alt="file_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>file_id : <em>string</em></strong></li>
  <li><img alt="tools" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>tools : <em>array of cluster</em></strong>
<ul>
  <li><img alt="incomplete_details" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="/_assets/shared-images/66/660aa55fd01c-response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
