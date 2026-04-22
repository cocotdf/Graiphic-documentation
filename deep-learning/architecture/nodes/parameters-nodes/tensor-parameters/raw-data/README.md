<h1>Raw Data Constant</h1>

<h2>Description</h2>

<p>Creates a constant node in the graph that outputs a tensor filled with a single repeated value. The scalar value is defined by <code>raw_data</code>, the output dimensions by <code>shape</code>, and the element type by <code>dtype</code>.</p>

<p align="center"><img alt="Raw Data" src="assets/Raw Data.png" width="263"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="32"/><strong>Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Unsigned_8.Png" src="/_assets/shared-images/f7/f7e8b09da0a0-input_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>raw_data : <em>array,</em></strong> represents the constant value that will populate the entire output tensor..</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Integer 32.Png" src="/_assets/shared-images/90/90ecefc445f7-array-integer-32.png" width="42"/></td>
      <td valign="top"><strong>shape : <em>array</em>, </strong>defines the dimensions of the output tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Enum.Png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="42"/></td>
      <td valign="top"><strong>dtype : <em>enum,</em></strong> specifies the type of the constant (e.g., <code>FLOAT</code>, <code>INT32</code>, <code>DOUBLE</code>).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name (optional) :</strong> <em><strong>string,</strong></em> name of the node.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="param_node_constant_raw" src="assets/param_node_constant_raw.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>Graph out : <em>object, </em></strong>ONNX model architecture.</td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
