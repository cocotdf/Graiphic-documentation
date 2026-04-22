<h1>CPU</h1>

<h2>Description</h2>

<p>Create CPU Session with its Session Options on the stored local Env. Type : polymorphic.</p>
<p align="center"><img src="/_assets/shared-images/46/46dbd4e24cd7-cpu.png" alt="CPU" width="270" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Inference in" src="/_assets/shared-images/13/13e0e5643b06-cacc__inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference in : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Sessions Parameters" src="/_assets/shared-images/1a/1a7a9a6249a8-ccclst.png" width="32"/> <strong>Sessions Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="intra_op_num_threads" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>intra_op_num_threads : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="inter_op_num_threads" src="/_assets/shared-images/e6/e64a060992b9-ci32.png" width="42"/></td>
      <td valign="top"><strong>inter_op_num_threads : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="execution_mode" src="/_assets/shared-images/7f/7f7e66ba54dc-cenum.png" width="42"/></td>
      <td valign="top"><strong>execution_mode : <em>enum</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="deterministic_compute" src="/_assets/shared-images/06/06612771a6c0-cbool.png" width="42"/></td>
      <td valign="top"><strong>deterministic_compute : <em>boolean</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="graph_optimization_level" src="/_assets/shared-images/d9/d9389531307d-cu16.png" width="42"/></td>
      <td valign="top"><strong>graph_optimization_level : <em>integer</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="optimized_model_file_path" src="/_assets/shared-images/09/0971eb44b0da-cpath.png" width="42"/></td>
      <td valign="top"><strong>optimized_model_file_path : <em>path</em></strong></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="profiling output dir" src="/_assets/shared-images/09/0971eb44b0da-cpath.png" width="42"/></td>
      <td valign="top"><strong>profiling output dir : <em>path</em></strong></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="Sessions Parameters" src="/_assets/shared-images/90/90bc1e7d81f2-sessions-parameters.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="model_path" src="/_assets/shared-images/09/0971eb44b0da-cpath.png" width="42"/></td>
      <td valign="top"><strong>model_path : <em>path</em></strong></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Inference out" src="/_assets/shared-images/d7/d7fa4da48d5e-iacc__inferencelvclass.png" width="42"/></td>
      <td valign="top"><strong>Inference out : <em>class</em></strong></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="EP By Node" src="/_assets/shared-images/fc/fcb3fe7c9ca3-i1dcclst.png" width="32"/> <strong>EP By Node : <em>array of cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="node_ep" src="/_assets/shared-images/48/48b3dacdc8e3-icclst.png" width="42"/></td>
      <td valign="top"><strong>node_ep : <em>cluster</em></strong>
<ul>
  <li><img alt="Execution Provider" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>Execution Provider : <em>string</em></strong></li>
  <li><img alt="Nodes Name" src="/_assets/shared-images/c4/c4de9f5441d0-i1dstr.png" width="32"/> <strong>Nodes Name : <em>array of string</em></strong>
<ul>
  <li><img alt="String" src="/_assets/shared-images/6d/6d824f6de01c-istr.png" width="32"/> <strong>String : <em>string</em></strong></li>
</ul></li>
  <li><img alt="Nb Nodes" src="/_assets/shared-images/c2/c25962a33cd0-iu32.png" width="32"/> <strong>Nb Nodes : <em>integer</em></strong></li>
</ul></td>
    </tr>
  </tbody>
</table>
      </td>
      <td valign="top" width="30%"><p align="center"><img alt="EP By Node" src="/_assets/shared-images/64/6476e4610014-ep-by-node.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>
