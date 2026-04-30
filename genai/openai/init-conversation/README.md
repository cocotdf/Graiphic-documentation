<h1>Init Conversation</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/init-conversation.png" alt="Init Conversation" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Assistants in" src="assets/cAssistantslvclass.png" width="42"/></td>
      <td valign="top"><strong>Assistants in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="assistant_parameters" src="assets/ccclst.png" width="32"/> <strong>assistant_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="model (required)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>model (required) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="name (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>name (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="description (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>description (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="instructions (optional)" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>instructions (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tools (optional)" src="assets/ctoolslvclass.png" width="42"/></td>
      <td valign="top"><strong>tools (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_resources (optional)" src="assets/ctool__resourceslvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_resources (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="assets/cmetadatalvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="temperature (optional)" src="assets/cdbl.png" width="42"/></td>
      <td valign="top"><strong>temperature (optional) : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="top_p (optional)" src="assets/cdbl.png" width="42"/></td>
      <td valign="top"><strong>top_p (optional) : <em>float</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="assistant_parameters" src="assets/assistant_parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="thread_parameters" src="assets/ccclst.png" width="32"/> <strong>thread_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="messages (optional)" src="assets/c1dcclst.png" width="42"/></td>
      <td valign="top"><strong>messages (optional) : <em>array of cluster</em></strong>
<ul>
  <li><img alt="role" src="assets/cstr.png" width="32"/> <strong>role : <em>string</em></strong></li>
  <li><img alt="content" src="assets/ccontentlvclass.png" width="32"/> <strong>content : <em>class</em></strong></li>
  <li><img alt="attachments" src="assets/c1dcclst.png" width="32"/> <strong>attachments : <em>array of cluster</em></strong>
<ul>
  <li><img alt="file_id" src="assets/cstr.png" width="32"/> <strong>file_id : <em>string</em></strong></li>
  <li><img alt="tools" src="assets/c1dcclst.png" width="32"/> <strong>tools : <em>array of cluster</em></strong>
<ul>
  <li><img alt="incomplete_details" src="assets/ccclst.png" width="32"/> <strong>incomplete_details : <em>cluster</em></strong>
<ul>
  <li><img alt="type" src="assets/cstr.png" width="32"/> <strong>type : <em>string</em></strong></li>
</ul></li>
</ul></li>
</ul></li>
  <li><img alt="metadata" src="assets/cmetadatalvclass.png" width="32"/> <strong>metadata : <em>class</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_resources (optional)" src="assets/ctool__resourceslvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_resources (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="assets/cmetadatalvclass.png" width="42"/></td>
      <td valign="top"><strong>metadata (optional) : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="thread_parameters" src="assets/thread_parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Assistants out" src="assets/iAssistantslvclass.png" width="42"/></td>
      <td valign="top"><strong>Assistants out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
