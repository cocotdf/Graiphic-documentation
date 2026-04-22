<h1>GatedRelativePositionBias</h1>

<h2>Description</h2>

<p>Setup and add GatedRelativePositionBias node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="assets/gatedrelativepositionbias.png" alt="GatedRelativePositionBias" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Graphs in" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Graphs in : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="query_layer" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>query_layer : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="query_bias" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>query_bias : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="rel_pos" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>rel_pos : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="weight" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>weight : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="bias" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>bias : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="eco_a" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>eco_a : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="token_offset" src="/_assets/shared-images/7b/7b301cd4aa9d-connxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>token_offset : <em>class</em></strong></td>
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
      <td width="64" valign="top"><img alt="num_heads" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="42"/></td>
      <td valign="top"><strong>num_heads : <em>integer</em></strong></td>
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
      <td width="64" valign="top"><img alt="output" src="/_assets/shared-images/1f/1f730a978528-ionnxmodellvclass.png" width="42"/></td>
      <td valign="top"><strong>output : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
