<h1>Edit Vector Store</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/edit-vector-store.png" alt="Edit Vector Store" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="/_assets/shared-images/77/7741fcb2046c-copenailvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="vector_store_id" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>vector_store_id : <em>string</em></strong></td>
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
      <td width="64" valign="top"><img alt="name (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>name (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_after (optional)" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="42"/></td>
      <td valign="top"><strong>expires_after (optional) : <em>cluster</em></strong>
<ul>
  <li><img alt="anchor (required)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>anchor (required) : <em>string</em></strong></li>
  <li><img alt="days (required)" src="/_assets/shared-images/4b/4b060a6ee305-cu32.png" width="32"/> <strong>days (required) : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata (optional) : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="request" src="assets/request.png" width="220"/></p></td>
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
      <td width="64" valign="top"><img alt="name" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="usage_bytes" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>usage_bytes : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="file_counts" src="/_assets/shared-images/b0/b0472b1126d2-inclst.png" width="42"/></td>
      <td valign="top"><strong>file_counts : <em>cluster</em></strong>
<ul>
  <li><img alt="in_progress" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>in_progress : <em>integer</em></strong></li>
  <li><img alt="completed" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>completed : <em>integer</em></strong></li>
  <li><img alt="failed" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>failed : <em>integer</em></strong></li>
  <li><img alt="cancelled" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>cancelled : <em>integer</em></strong></li>
  <li><img alt="total" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>total : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="status" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="42"/></td>
      <td valign="top"><strong>status : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_after" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>expires_after : <em>cluster</em></strong>
<ul>
  <li><img alt="anchor" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>anchor : <em>string</em></strong></li>
  <li><img alt="days" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>days : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>expires_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="last_active_at" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="42"/></td>
      <td valign="top"><strong>last_active_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata" src="/_assets/shared-images/a5/a5c2d660da20-igguflvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="/_assets/shared-images/4b/4b03063a8ded-response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
