<h1>Convert Raw Data Cluster Array To CUDA Ptr Cluster Array</h1>

<h2>Description</h2>

<p>Allocate and copy data to Cuda Ptr for all inputs and store the ptr into the cluster. Warning : The Cuda Ptr allocated by this functions need to be free. Type : polymorphic.</p>
<p align="center"><img src="assets/convert-raw-data-cluster-array-to-cuda-ptr-cluster-array.png" alt="Convert Raw Data Cluster Array To CUDA Ptr Cluster Array" width="270" /></p>

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
  <li><img alt="inputs_data" src="assets/c1du8.png" width="32"/> <strong>inputs_data : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/cu8.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_shapes" src="assets/c1di64.png" width="32"/> <strong>inputs_shapes : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs string length" src="assets/c1di64.png" width="32"/> <strong>inputs string length : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_ranks" src="assets/c1di64.png" width="32"/> <strong>inputs_ranks : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_types" src="assets/c1denum.png" width="32"/> <strong>inputs_types : <em>array of enum</em></strong>
<ul>
  <li><img alt="dtype" src="assets/cenum.png" width="32"/> <strong>dtype : <em>enum</em></strong></li>
</ul></li>
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

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Data in" src="assets/i1dcclst.png" width="32"/> <strong>Data in : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="frw_input_cluster" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>frw_input_cluster : <em>cluster</em></strong>
<ul>
  <li><img alt="input_order" src="assets/iu32.png" width="32"/> <strong>input_order : <em>integer</em></strong></li>
  <li><img alt="Inputs Info" src="assets/icclst.png" width="32"/> <strong>Inputs Info : <em>cluster</em></strong>
<ul>
  <li><img alt="inputs_ptr" src="assets/iu64.png" width="32"/> <strong>inputs_ptr : <em>integer</em></strong></li>
  <li><img alt="inputs_shapes" src="assets/i1di64.png" width="32"/> <strong>inputs_shapes : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="assets/ii64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_ranks" src="assets/ii64.png" width="32"/> <strong>inputs_ranks : <em>integer</em></strong></li>
  <li><img alt="inputs_types" src="assets/ienum.png" width="32"/> <strong>inputs_types : <em>enum</em></strong></li>
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
