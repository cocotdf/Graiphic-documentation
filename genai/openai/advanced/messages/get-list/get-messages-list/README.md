<h1>Get Messages List</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/get-messages-list.png" alt="Get Messages List" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="/_assets/shared-images/77/7741fcb2046c-copenailvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="thread_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>thread_id : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="limit (optional)" src="/_assets/shared-images/ef/efab0cbdbf3e-cu8.png" width="42"/></td>
      <td valign="top"><strong>limit (optional) : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="order (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>order (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="after (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>after (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="before (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>before (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="run_id (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>run_id (optional) : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="parameters" src="/_assets/shared-images/db/db4e15ec2d0a-parameters.png" width="220"/></p></td>
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
      <td width="64" valign="top"><img alt="object" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>object : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="data" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="42"/></td>
      <td valign="top"><strong>data : <em>array of cluster</em></strong>
<ul>
  <li><img alt="response" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>response : <em>cluster</em></strong>
<ul>
  <li><img alt="id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>id : <em>string</em></strong></li>
  <li><img alt="object" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>object : <em>string</em></strong></li>
  <li><img alt="created_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>created_at : <em>integer</em></strong></li>
  <li><img alt="thread_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>thread_id : <em>string</em></strong></li>
  <li><img alt="status" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>status : <em>string</em></strong></li>
  <li><img alt="incomplete_details" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="reason" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>reason : <em>string</em></strong></li>
</ul></li>
  <li><img alt="completed_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>completed_at : <em>integer</em></strong></li>
  <li><img alt="incomplete_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>incomplete_at : <em>integer</em></strong></li>
  <li><img alt="role" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>role : <em>string</em></strong></li>
  <li><img alt="content" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="32"/> <strong>content : <em>class</em></strong></li>
  <li><img alt="assistant_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>assistant_id : <em>string</em></strong></li>
  <li><img alt="run_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>run_id : <em>string</em></strong></li>
  <li><img alt="attachments" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>attachments : <em>array of cluster</em></strong>
<ul>
  <li><img alt="file_id" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>file_id : <em>string</em></strong></li>
  <li><img alt="tools" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>tools : <em>array of cluster</em></strong>
<ul>
  <li><img alt="incomplete_details" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>type : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></li>
  <li><img alt="metadata" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="32"/> <strong>metadata : <em>class</em></strong></li>
</ul></li>
</ul></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="assets/response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
