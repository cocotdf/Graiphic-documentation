<h1>Train Output</h1>

<h2>Description</h2>

<p>Setup and add “Output Train” node into the model during the definition graph step.</p>

<p align="center"><img alt="enum.png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="237"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer, </em></strong>this parameter refers to the position of the input within the ONNX graph. When executing a model with multiple inputs, the index helps you identify which input you are targeting. It is especially useful when configuring input data, using the <strong>Input Data</strong> polymorph found in the <strong>Deep Learning</strong> → <strong>Runtime</strong> palette.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>Graph in : <em>object,</em></strong> ONNX model architecture.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="32"/><strong>Parameters : <em>cluster</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Enum.Png" src="/_assets/shared-images/9d/9d61ac752ae1-enum.png" width="42"/></td>
      <td valign="top"><strong>dtype <em>: enum, </em></strong>the data type for the elements of the output tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “FLOAT”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong><a href="../../define-deep-learning-architecture/losses/resume-9/README.md">Loss</a> :</strong> <em><strong>cluster,</strong></em> this cluster defines the loss function used for model training.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="output_object.png" src="/_assets/shared-images/1c/1cb1833f6933-output_object.png" width="42"/></td>
      <td valign="top"><strong>enum :</strong> <em><strong>enum</strong></em>, an enumeration indicating the loss type (e.g., MSE, CrossEntropy, etc.). If <code>enum</code> is set to <code>CustomLoss</code>, the custom class on the right will be used as the loss function. Otherwise, the selected loss will be applied with its default configuration.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="node_train_output.png" src="assets/node_train_output.png" width="42"/></td>
      <td valign="top"><strong>Class :</strong> <em><strong>object</strong></em>, a custom loss class instance.</td>
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
      <td valign="top" width="30%"><p align="center"><img alt="param_node_train_output" src="assets/param_node_train_output.png" width="220"/></p></td>
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
