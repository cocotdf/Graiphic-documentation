<h1>Get Vector Stores List</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/get-vector-stores-list.png" alt="Get Vector Stores List" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="OpenAI in" src="assets/cOpenAIlvclass.png" width="42"/></td>
      <td valign="top"><strong>OpenAI in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="parameters" src="assets/ccclst.png" width="32"/> <strong>parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="limit (optional)" src="assets/cu8.png" width="42"/></td>
      <td valign="top"><strong>limit (optional) : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="order (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>order (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="after (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>after (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="before (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>before (optional) : <em>string</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="parameters" src="assets/parameters.png" width="220"/></p></td>
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
      <td width="64" valign="top"><img alt="object" src="assets/istr.png" width="42"/></td>
      <td valign="top"><strong>object : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="data" src="assets/i1dcclst.png" width="42"/></td>
      <td valign="top"><strong>data : <em>array of cluster</em></strong>
<ul>
  <li><img alt="response" src="assets/icclst.png" width="32"/> <strong>response : <em>cluster</em></strong>
<ul>
  <li><img alt="id" src="assets/istr.png" width="32"/> <strong>id : <em>string</em></strong></li>
  <li><img alt="object" src="assets/istr.png" width="32"/> <strong>object : <em>string</em></strong></li>
  <li><img alt="created_at" src="assets/iu32.png" width="32"/> <strong>created_at : <em>integer</em></strong></li>
  <li><img alt="name" src="assets/istr.png" width="32"/> <strong>name : <em>string</em></strong></li>
  <li><img alt="usage_bytes" src="assets/iu32.png" width="32"/> <strong>usage_bytes : <em>integer</em></strong></li>
  <li><img alt="file_counts" src="assets/inclst.png" width="32"/> <strong>file_counts : <em>cluster</em></strong>
<ul>
  <li><img alt="in_progress" src="assets/iu32.png" width="32"/> <strong>in_progress : <em>integer</em></strong></li>
  <li><img alt="completed" src="assets/iu32.png" width="32"/> <strong>completed : <em>integer</em></strong></li>
  <li><img alt="failed" src="assets/iu32.png" width="32"/> <strong>failed : <em>integer</em></strong></li>
  <li><img alt="cancelled" src="assets/iu32.png" width="32"/> <strong>cancelled : <em>integer</em></strong></li>
  <li><img alt="total" src="assets/iu32.png" width="32"/> <strong>total : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="status" src="assets/istr.png" width="32"/> <strong>status : <em>string</em></strong></li>
  <li><img alt="expires_after" src="assets/icclst.png" width="32"/> <strong>expires_after : <em>cluster</em></strong>
<ul>
  <li><img alt="anchor" src="assets/istr.png" width="32"/> <strong>anchor : <em>string</em></strong></li>
  <li><img alt="days" src="assets/iu32.png" width="32"/> <strong>days : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="expires_at" src="assets/iu32.png" width="32"/> <strong>expires_at : <em>integer</em></strong></li>
  <li><img alt="last_active_at" src="assets/iu32.png" width="32"/> <strong>last_active_at : <em>integer</em></strong></li>
  <li><img alt="metadata" src="assets/imetadatalvclass.png" width="32"/> <strong>metadata : <em>class</em></strong></li>
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
