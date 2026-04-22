<h1>Init Conversation</h1>

<h2>Description</h2>

<p>Type : VI.</p>

<p align="center"><img src="assets/init-conversation.png" alt="Init Conversation" width="270" /></p>

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
      <td valign="top" width="70%"><p><img alt="assistant_parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>assistant_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="model (required)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>model (required) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="name (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>name (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="description (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>description (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="instructions (optional)" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>instructions (optional) : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tools (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tools (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="tool_resources (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_resources (optional) : <em>class</em></strong></td>
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
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="assistant_parameters" src="/_assets/shared-images/d8/d81b3ef4a3d9-request.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="thread_parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>thread_parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="messages (optional)" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="42"/></td>
      <td valign="top"><strong>messages (optional) : <em>array of cluster</em></strong>
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
      <td width="64" valign="top"><img alt="tool_resources (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
      <td valign="top"><strong>tool_resources (optional) : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="metadata (optional)" src="/_assets/shared-images/d0/d02f3e0bb4c0-cgguflvclass.png" width="42"/></td>
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
      <td width="64" valign="top"><img alt="Assistants out" src="/_assets/shared-images/80/80afcce65438-iopenailvclass.png" width="42"/></td>
      <td valign="top"><strong>Assistants out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
