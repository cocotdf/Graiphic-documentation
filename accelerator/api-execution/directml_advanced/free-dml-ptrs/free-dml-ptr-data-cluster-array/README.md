<h1>Free DML Ptr Data Cluster Array</h1>

<h2>Description</h2>

<p>Free all the ptrs inside the Data in array. Type : VI.</p>
<p align="center"><img src="assets/free-dml-ptr-data-cluster-array.png" alt="Free DML Ptr Data Cluster Array" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Data in" src="assets/c1dcclst.png" width="32"/> <strong>Data in : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="frw_input_cluster" src="assets/ccclst.png" width="42"/></td>
      <td valign="top"><strong>frw_input_cluster : <em>cluster</em></strong>
<ul>
  <li><img alt="input_order" src="assets/cu32.png" width="32"/> <strong>input_order : <em>integer</em></strong></li>
  <li><img alt="Inputs Info" src="assets/ccclst.png" width="32"/> <strong>Inputs Info : <em>cluster</em></strong>
<ul>
  <li><img alt="inputs_ptr" src="assets/cu64.png" width="32"/> <strong>inputs_ptr : <em>integer</em></strong></li>
  <li><img alt="inputs_shapes" src="assets/c1di64.png" width="32"/> <strong>inputs_shapes : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_ranks" src="assets/ci64.png" width="32"/> <strong>inputs_ranks : <em>integer</em></strong></li>
  <li><img alt="inputs_types" src="assets/cenum.png" width="32"/> <strong>inputs_types : <em>enum</em></strong></li>
</ul></li>
</ul></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Data in" src="assets/Data in.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Inference in" src="assets/cacc__Inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Inference out" src="assets/iacc__Inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
