<h1>DequantizeLinear</h1>

<h2>Description</h2>

<p>Setup and add DequantizeLinear node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="assets/dequantizelinear.png" alt="DequantizeLinear" width="270" /></p>

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
      <td width="64" valign="top"><img alt="x_scale" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>x_scale : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="x_zero_point" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>x_zero_point : <em>class</em></strong></td>
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
      <td width="64" valign="top"><img alt="axis" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="42"/></td>
      <td valign="top"><strong>axis : <em>cluster</em></strong>
<ul>
  <li><img alt="value" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="32"/> <strong>value : <em>integer</em></strong></li>
  <li><img alt="use_it" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="32"/> <strong>use_it : <em>boolean</em></strong></li>
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
      <td width="64" valign="top"><img alt="y" src="/_assets/shared-images/1f/1f730a978528-ionnxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>y : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
