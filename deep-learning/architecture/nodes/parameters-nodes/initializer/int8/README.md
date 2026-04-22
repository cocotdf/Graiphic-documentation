<h1>Int8 Initializer</h1>

<h2>Description</h2>

<p>Creates a graph initializer of type <code>int8</code>. The data is provided through the parameters and stored as a fixed initializer inside the graph.</p>

<p align="center"><img alt="Int8" src="assets/Int8.png" width="263"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong>Parameters : <em>cluster</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="node_initializer_int8.png" src="/_assets/shared-images/1e/1e799ebf5691-node_initializer_int8.png" width="42"/></td>
      <td valign="top"><strong>flattened_int8_data : <em>array,</em></strong> stores the explicit list of numeric values for the initializer, in a flattened one-dimensional format.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Integer 32.Png" src="/_assets/shared-images/90/90ecefc445f7-array-integer-32.png" width="42"/></td>
      <td valign="top"><strong>shape : <em>array</em>, </strong>defines the true shape of the initializer tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong>Training : <em>cluster, </em></strong>these parameters only have an effect in a training graph.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Enum.Png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="42"/></td>
      <td valign="top"><strong><a href="../../../../../more-deep-learning/nodes-parameters/training_type/README.md">type</a> : <em>enum, </em></strong>defines how the initializer behaves when the graph is used in training mode. It determines whether the tensor is treated as a constant, as trainable weights, or as frozen weights. During inference, it makes no difference whether the type is <code>Constant</code>, <code>Train Weights</code>, or <code>Frozen Weights</code>.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><a href="../../../../../more-deep-learning/layers-parameters/regularizer/README.md">Regularizer</a> : <em>cluster, </em>regularizer function applied to the weights matrix.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name (optional) :</strong> <em><strong>string,</strong></em> name of the node.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="param_node_initializer_int8" src="assets/param_node_initializer_int8.png" width="220"/></p></td>
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
