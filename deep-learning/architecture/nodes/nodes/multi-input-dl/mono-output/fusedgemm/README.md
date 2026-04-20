<h1>FusedGemm</h1>

<h2>Description</h2>

<p>Setup and add FusedGemm node into the model during the definition graph step. Type : polymorphic.</p>
<p align="center"><img src="assets/fusedgemm.png" alt="FusedGemm" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Graphs in" src="assets/ccclst.png" width="32"/> <strong>Graphs in : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="A" src="assets/cONNXModellvclass.png" width="42"/></td>
      <td valign="top"><strong>A : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="B" src="assets/cONNXModellvclass.png" width="42"/></td>
      <td valign="top"><strong>B : <em>class</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="C" src="assets/cONNXModellvclass.png" width="42"/></td>
      <td valign="top"><strong>C : <em>class</em></strong></td>
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
      <td valign="top" width="70%"><p><img alt="Parameters" src="assets/ccclst.png" width="32"/> <strong>Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="activation" src="assets/cenum.png" width="42"/></td>
      <td valign="top"><strong>activation : <em>enum</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="activation_alpha" src="assets/csgl.png" width="42"/></td>
      <td valign="top"><strong>activation_alpha : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="activation_beta" src="assets/csgl.png" width="42"/></td>
      <td valign="top"><strong>activation_beta : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="activation_gamma" src="assets/csgl.png" width="42"/></td>
      <td valign="top"><strong>activation_gamma : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="alpha" src="assets/csgl.png" width="42"/></td>
      <td valign="top"><strong>alpha : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="beta" src="assets/csgl.png" width="42"/></td>
      <td valign="top"><strong>beta : <em>float</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="transA" src="assets/cbool.png" width="42"/></td>
      <td valign="top"><strong>transA : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="transB" src="assets/cbool.png" width="42"/></td>
      <td valign="top"><strong>transB : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="training?" src="assets/cbool.png" width="42"/></td>
      <td valign="top"><strong>training? : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="lda coeff" src="assets/cdbl.png" width="42"/></td>
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
      <td width="64" valign="top"><img alt="name" src="assets/cstr.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="specified_outputs_name" src="assets/c1dstr.png" width="42"/></td>
      <td valign="top"><strong>specified_outputs_name : <em>array of string</em></strong>
<ul>
  <li><img alt="String" src="assets/cstr.png" width="32"/> <strong>String : <em>string</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Y" src="assets/iONNXModellvclass.png" width="42"/></td>
      <td valign="top"><strong>Y : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
