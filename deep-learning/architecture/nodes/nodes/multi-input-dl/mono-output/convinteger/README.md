<h1>ConvInteger</h1>

<h2>Description</h2>

<p>Setup and add ConvInteger node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="/_assets/shared-images/c0/c092b4989e7f-convinteger.png" alt="ConvInteger" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Graphs in" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Graphs in : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="x" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>x : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="w" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>w : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="x_zero_point" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>x_zero_point : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="w_zero_point" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>w_zero_point : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Graphs in" src="assets/Graphs in.png" width="220"/></p></td>
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
      <td valign="top" width="30%"><p align="center"><img alt="Parameters" src="/_assets/shared-images/70/70fb503c2fef-parameters.png" width="220"/></p></td>
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
      <td width="64" valign="top"><img alt="y" src="/_assets/shared-images/1f/1f730a978528-ionnxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>y : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
