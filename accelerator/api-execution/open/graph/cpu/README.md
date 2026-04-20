<h1>CPU</h1>

<h2>Description</h2>

<p>Generate the ONNX Graph then create a CPU Session from it. Type : polymorphic.</p>
<p align="center"><img src="assets/cpu.png" alt="CPU" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Model in" src="assets/cacc__Modellvclass.png" width="42"/></td>
      <td valign="top"><strong>Model in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Sessions Parameters" src="assets/ccclst.png" width="32"/> <strong>Sessions Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="intra_op_num_threads" src="assets/ci32.png" width="42"/></td>
      <td valign="top"><strong>intra_op_num_threads : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="inter_op_num_threads" src="assets/ci32.png" width="42"/></td>
      <td valign="top"><strong>inter_op_num_threads : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="execution_mode" src="assets/cenum.png" width="42"/></td>
      <td valign="top"><strong>execution_mode : <em>enum</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="deterministic_compute" src="assets/cbool.png" width="42"/></td>
      <td valign="top"><strong>deterministic_compute : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="graph_optimization_level" src="assets/cu16.png" width="42"/></td>
      <td valign="top"><strong>graph_optimization_level : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="optimized_model_file_path" src="assets/cpath.png" width="42"/></td>
      <td valign="top"><strong>optimized_model_file_path : <em>path</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="profiling output dir" src="assets/cpath.png" width="42"/></td>
      <td valign="top"><strong>profiling output dir : <em>path</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Sessions Parameters" src="assets/Sessions Parameters.png" width="220"/></p></td>
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

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="EP By Node" src="assets/i1dcclst.png" width="32"/> <strong>EP By Node : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="node_ep" src="assets/icclst.png" width="42"/></td>
      <td valign="top"><strong>node_ep : <em>cluster</em></strong>
<ul>
  <li><img alt="Execution Provider" src="assets/istr.png" width="32"/> <strong>Execution Provider : <em>string</em></strong></li>
  <li><img alt="Nodes Name" src="assets/i1dstr.png" width="32"/> <strong>Nodes Name : <em>array of string</em></strong>
<ul>
  <li><img alt="String" src="assets/istr.png" width="32"/> <strong>String : <em>string</em></strong></li>
</ul></li>
  <li><img alt="Nb Nodes" src="assets/iu32.png" width="32"/> <strong>Nb Nodes : <em>integer</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="EP By Node" src="assets/EP By Node.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
