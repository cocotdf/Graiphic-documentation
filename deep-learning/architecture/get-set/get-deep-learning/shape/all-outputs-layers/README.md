<h1>All outputs layers shape</h1>

<h2>Description</h2>

<p>Gets the output form of the model.</p>

<p align="center"><img alt="get_all_input_shape" src="/_assets/shared-images/37/373d37e69858-get_all_input_shape.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
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
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster Array Out.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="42"/></td>
      <td valign="top"><strong>output_array : <em>array,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="42"/></td>
      <td valign="top"><strong>Name : <em>cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>node : <em>string</em>,</strong> name of the ONNX node producing the output (e.g., <code>Dense_342_output</code>).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>output : <em>string</em>,</strong> identifier of the output tensor from this node.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>,</strong> index of the node within the ONNX graph, used to perform <code>get</code> or <code>set</code> operations on a specific node.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>output_order : <em>integer</em>,</strong> index of the output (useful to retrieve the data after execution if there are multiple outputs).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Out Array Integer 32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top"><strong>output_shape : <em>array</em>,</strong> expected shape of the output tensor. This shape is only valid for models using explicit <code>Layers</code>, and the first dimension always corresponds to the batch size (even if shown as 1 here).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="output_enum.png" src="/_assets/shared-images/a0/a0e1d8d91545-output_enum.png" width="42"/></td>
      <td valign="top"><strong>dtype : <em>enum, </em></strong>data type of the output tensor (e.g., <code>FLOAT</code> for floating-point tensors).</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_shape_array" src="/_assets/shared-images/98/98771bf73d95-output_shape_array.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>

<h3>Using the “Get All Output Layer Shape” function</h3>

<p align="center"><img alt="get_all_output_layer_shape" src="assets/get_all_output_layer_shape.png" width="220"/></p>

<p>1 – Define Graph</p>

<p>We define two graphs with two dense layers each and an input of different size.</p>

<p>2 – Merge Function</p>

<p>We use the “Merge” function to merge the two graphs.</p>

<p>3 – Get Function</p>

<p>We use the function “Get All Output Layer Shape” to get the output(s) form of the model.</p>
