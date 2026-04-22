<h1>Output Train</h1>

<h2>Description</h2>

<p>Setup and add the output layer into the model during the definition graph step. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/56/565c52bff932-output_train_add_to_graph.png" alt="Output_Train_Add_To_Graph.Png" width="253" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Out Array Integer 32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer, </em></strong>position of the output in the graph. This is used only if the <strong>Runtime</strong> → <strong>Output Data VI</strong>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="../../../../_resolved/and/assets/cluster.png" width="42"/></td>
      <td valign="top"><strong>Parameters : <em>cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Enum.Png" src="/_assets/shared-images/93/9363ce0bc3eb-output_array_enum.png" width="42"/></td>
      <td valign="top"><strong>dtype</strong><strong> :</strong> <em><strong>enum,</strong></em> data type of the input tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="../../../../_resolved/and/assets/cluster.png" width="42"/></td>
      <td valign="top"><strong><a href="../../define-deep-learning-architecture/losses/resume-9/README.md">Loss</a> : <em>cluster, </em></strong>measures the difference between the model’s predictions and the expected values, helping guide the learning process.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Model.Png" src="/_assets/shared-images/3c/3c881c79a647-output_model.png" width="42"/></td>
      <td valign="top"><strong>Model out : </strong>model architecture.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>output name : <em>string, </em></strong>name assigned to the output in the graph.</td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<h3>Input shape</h3>

<p>Input tensor (of any rank).</p>

<h3>Output shape</h3>

<p>Same shape as input.</p>
