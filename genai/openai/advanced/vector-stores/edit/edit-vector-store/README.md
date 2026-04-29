<h1>Edit Vector Store</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/edit-vector-store.png" alt="Edit Vector Store" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="assets/cOpenAIlvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="vector_store_id" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>vector_store_id : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="request" src="assets/ccclst.png" width="32"/> <strong>request : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="name (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>name (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_after (optional)" src="assets/ccclst.png" width="42"/></td>
      <td valign="top"><strong>expires_after (optional) : <em>cluster</em></strong>
<ul>
  <li><img alt="anchor (required)" src="assets/cstr.png" width="32"/> <strong>anchor (required) : <em>string</em></strong></li>
  <li><img alt="days (required)" src="assets/cu32.png" width="32"/> <strong>days (required) : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="assets/cmetadatalvclass.png" width="42"/></td>
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
      <td width="64" valign="top"><img alt="name" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="usage_bytes" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>usage_bytes : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="file_counts" src="assets/inclst.png" width="42"/></td>
      <td valign="top"><strong>file_counts : <em>cluster</em></strong>
<ul>
  <li><img alt="in_progress" src="assets/iu32.png" width="32"/> <strong>in_progress : <em>integer</em></strong></li>
  <li><img alt="completed" src="assets/iu32.png" width="32"/> <strong>completed : <em>integer</em></strong></li>
  <li><img alt="failed" src="assets/iu32.png" width="32"/> <strong>failed : <em>integer</em></strong></li>
  <li><img alt="cancelled" src="assets/iu32.png" width="32"/> <strong>cancelled : <em>integer</em></strong></li>
  <li><img alt="total" src="assets/iu32.png" width="32"/> <strong>total : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="status" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>status : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_after" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>expires_after : <em>cluster</em></strong>
<ul>
  <li><img alt="anchor" src="assets/istr.png" width="32"/> <strong>anchor : <em>string</em></strong></li>
  <li><img alt="days" src="assets/iu32.png" width="32"/> <strong>days : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="expires_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>expires_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="last_active_at" src="assets/iu32.png" width="42"/></td>
      <td valign="top"><strong>last_active_at : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata" src="assets/imetadatalvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="response" src="assets/response.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
