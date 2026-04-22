<h1>Convert Raw Data Cluster Array To DML Ptr Cluster Array</h1>

<h2>Description</h2>

<p>Allocate and copy data to DirectML Ptr for all inputs and store the ptr into the cluster. Warning : The DirectML Ptr allocated by this functions need to be free. You also need to link a valid DirectML Execution Session. Type : polymorphic.</p>
<p align="center"><img src="assets/convert-raw-data-cluster-array-to-dml-ptr-cluster-array.png" alt="Convert Raw Data Cluster Array To DML Ptr Cluster Array" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Data in" src="/_assets/shared-images/d3/d34232a0665a-c1dcclst.png" width="32"/> <strong>Data in : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="frw_input_cluster" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="42"/></td>
      <td valign="top"><strong>frw_input_cluster : <em>cluster</em></strong>
<ul>
  <li><img alt="input_order" src="/_assets/shared-images/4b/4b060a6ee305-cu32.png" width="32"/> <strong>input_order : <em>integer</em></strong></li>
  <li><img alt="Inputs Info" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Inputs Info : <em>cluster</em></strong>
<ul>
  <li><img alt="inputs_data" src="/_assets/shared-images/a0/a042170529ac-c1du8.png" width="32"/> <strong>inputs_data : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/ef/efab0cbdbf3e-cu8.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_shapes" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="32"/> <strong>inputs_shapes : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs string length" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="32"/> <strong>inputs string length : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_ranks" src="/_assets/shared-images/a4/a466ab17832c-c1di64.png" width="32"/> <strong>inputs_ranks : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/b6/b6c25b5c1c13-ci64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_types" src="/_assets/shared-images/30/30a3bcf08436-c1denum.png" width="32"/> <strong>inputs_types : <em>array of enum</em></strong>
<ul>
  <li><img alt="dtype" src="/_assets/shared-images/7f/7f7e66ba54dc-cenum.png" width="32"/> <strong>dtype : <em>enum</em></strong></li>
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

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Inference in" src="/_assets/shared-images/13/13e0e5643b06-cacc__inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Data in" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>Data in : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="frw_input_cluster" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>frw_input_cluster : <em>cluster</em></strong>
<ul>
  <li><img alt="input_order" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>input_order : <em>integer</em></strong></li>
  <li><img alt="Inputs Info" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="32"/> <strong>Inputs Info : <em>cluster</em></strong>
<ul>
  <li><img alt="inputs_ptr" src="/_assets/shared-images/77/77acaca6b85f-iu64.png" width="32"/> <strong>inputs_ptr : <em>integer</em></strong></li>
  <li><img alt="inputs_shapes" src="/_assets/shared-images/fd/fdc8b92d3fb6-i1di64.png" width="32"/> <strong>inputs_shapes : <em>array of integer</em></strong>
<ul>
  <li><img alt="Numeric" src="/_assets/shared-images/26/264967b65e8e-ii64.png" width="32"/> <strong>Numeric : <em>integer</em></strong></li>
</ul></li>
  <li><img alt="inputs_ranks" src="/_assets/shared-images/26/264967b65e8e-ii64.png" width="32"/> <strong>inputs_ranks : <em>integer</em></strong></li>
  <li><img alt="inputs_types" src="/_assets/shared-images/b4/b48b0be5e324-ienum.png" width="32"/> <strong>inputs_types : <em>enum</em></strong></li>
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
      <td width="64" valign="top"><img alt="Inference out" src="/_assets/shared-images/d7/d7fa4da48d5e-iacc__inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>
