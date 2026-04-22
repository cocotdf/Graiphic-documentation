<h1>ConvTranspose</h1>

<h2>Description</h2>

<p>Setup and add ConvTransposeNode node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="assets/convtranspose.png" alt="ConvTranspose" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Graphs in" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Graphs in : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="X" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>X : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="W" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>W : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="B" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>B : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Graphs in" src="/_assets/shared-images/d9/d97578b00f6a-graphs-in.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="auto_pad" src="/_assets/shared-images/7f/7f7e66ba54dc-cenum.png" width="42"/></td>
      <td valign="top"><strong>auto_pad : <em>enum</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="dilations" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>dilations : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="group" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>group : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="kernel_shape" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>kernel_shape : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="output_padding" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>output_padding : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="output_shape" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>output_shape : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="pads" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>pads : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="strides" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="42"/></td>
      <td valign="top"><strong>strides : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="training?" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>training? : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="lda coeff" src="/_assets/shared-images/c7/c71945e6f909-cdbl.png" width="42"/></td>
      <td valign="top"><strong>lda coeff : <em>float</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Parameters" src="assets/Parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="name" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="specified_outputs_name" src="/_assets/shared-images/ce/ceeb813734df-c1dstr.png" width="42"/></td>
      <td valign="top"><strong>specified_outputs_name : <em>array of string</em></strong>
<ul>
  <li><img alt="String" src="/_assets/shared-images/71/714be290bc5b-cstr.png" width="32"/> <strong>String : <em>string</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Y" src="/_assets/shared-images/1f/1f730a978528-ionnxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>Y : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
