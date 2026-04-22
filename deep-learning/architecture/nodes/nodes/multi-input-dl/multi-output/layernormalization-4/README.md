<h1>LayerNormalization</h1>

<h2>Description</h2>

<p>This is layer normalization defined in ONNX as function. The overall computation can be split into two stages. The first stage is standardization, which makes the normalized elements have zero mean and unit variances.</p>

<p align="center"><img alt="node_batch_norm.png" src="/_assets/shared-images/89/89b307a3d5a3-node_batch_norm.png" width="311"/></p>

<p>The computation required by standardization can be described by the following equations.</p>

<p>Mean</p>

<p>=</p>

<p>ReduceMean</p>

<p>&lt;</p>

<p>axes</p>

<p>=</p>

<p>normalized_axes</p>

<p>&gt;</p>

<p>(</p>

<p>X</p>

<p>)</p>

<p>D</p>

<p>=</p>

<p>Sub</p>

<p>(</p>

<p>X</p>

<p>,</p>

<p>Mean</p>

<p>)</p>

<p>DD</p>

<p>=</p>

<p>Mul</p>

<p>(</p>

<p>D</p>

<p>,</p>

<p>D</p>

<p>)</p>

<p>Var</p>

<p>=</p>

<p>ReduceMean</p>

<p>&lt;</p>

<p>axes</p>

<p>=</p>

<p>normalized_axes</p>

<p>&gt;</p>

<p>(</p>

<p>DD</p>

<p>)</p>

<p>VarEps</p>

<p>=</p>

<p>Add</p>

<p>(</p>

<p>Var</p>

<p>,</p>

<p>epsilon</p>

<p>)</p>

<p>StdDev</p>

<p>=</p>

<p>Sqrt</p>

<p>(</p>

<p>VarEps</p>

<p>)</p>

<p>InvStdDev</p>

<p>=</p>

<p>Reciprocal</p>

<p>(</p>

<p>StdDev</p>

<p>)</p>

<p>Normalized</p>

<p>=</p>

<p>Mul</p>

<p>(</p>

<p>D</p>

<p>,</p>

<p>InvStdDev</p>

<p>)</p>

<p>where <code>normalized_axes</code> is <code>[axis, ..., rank of X - 1]</code>. The variables <code>Var</code> and <code>StdDev</code> stand for variance and standard deviation, respectively. The second output is <code>Mean</code> and the last one is <code>InvStdDev</code>. Depending on <code>stash_type</code> attribute, the actual computation must happen in different floating-point precision. For example, if <code>stash_type</code> is 1, this operator casts all input variables to 32-bit float, perform the computation, and finally cast <code>Normalized</code> back to the original type of <code>X</code>. The second stage then scales and shifts the outcome of the first stage using</p>

<p>NormalizedScaled</p>

<p>=</p>

<p>Mul</p>

<p>(</p>

<p>Normalized</p>

<p>,</p>

<p>Scale</p>

<p>)</p>

<p>Y</p>

<p>=</p>

<p>Add</p>

<p>(</p>

<p>NormalizedScaled</p>

<p>,</p>

<p>B</p>

<p>)</p>

<p>The second stage doesn’t depends on <code>stash_type</code>. All equations are in <a href="https://github.com/onnx/onnx/blob/main/docs/Syntax.md">this syntax</a>. The same variable (i.e., input, output, and attribute) uses the same name in the equations above and this operator’s definition. Let <code>d</code> indicate the i-th dimension of <code>X</code>. If <code>X</code>’s shape is <code>[d[0], ..., d[axis-1], d[axis], ..., d[rank-1]]</code>, the shape of <code>Mean</code> and <code>InvStdDev</code> is <code>[d[0], ..., d[axis-1], 1, ..., 1]</code>. <code>Y</code> and <code>X</code> have the same shape. This operator supports unidirectional broadcasting (tensors <code>Scale</code> and <code>B</code> should be unidirectional broadcastable to tensor <code>X</code>); for more details please check <a href="https://github.com/onnx/onnx/blob/main/docs/Broadcasting.md">Broadcasting in ONNX</a>.</p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_String.Png" src="/_assets/shared-images/60/600c0aac18dc-input_array_string.png" width="42"/></td>
      <td valign="top"><strong><a href="../../../../../../more-deep-learning/nodes-parameters/specified_outputs_name/README.md">specified_outputs_name</a> : <em>array, </em></strong>this parameter lets you manually assign custom names to the output tensors of a node.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong>Graphs in :</strong> <strong><em>cluster,</em></strong> ONNX model architecture.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>X (heterogeneous) – T : <em>object, </em></strong>tensor to be normalized.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>Scale (heterogeneous) – T : <em>object, </em></strong>scale tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>B (optional, heterogeneous) – T : <em>object, </em></strong>bias tensor.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_node_layer_norm" src="assets/input_node_layer_norm.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong>Parameters : <em>cluster,</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_64.Png" src="/_assets/shared-images/c9/c9a23cc7d835-input_interger_64.png" width="42"/></td>
      <td valign="top"><strong>axis : <em>integer,</em></strong> the first normalization dimension. If rank(X) is r, axis’ allowed range is [-r, r). Negative value means counting dimensions from the back.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “-1”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Single.Png" src="/_assets/shared-images/e2/e22146c46f27-single.png" width="42"/></td>
      <td valign="top"><strong>epsilon : <em>float,</em></strong> the epsilon value to use to avoid division by zero.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “1e-05”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Interger_64.Png" src="/_assets/shared-images/c9/c9a23cc7d835-input_interger_64.png" width="42"/></td>
      <td valign="top"><strong>stash_type :</strong> <strong><em>integer</em></strong>, type of Mean and InvStdDev. This also specifies stage one’s computation precision.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “1”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Booleen.Png" src="/_assets/shared-images/e9/e9f30799ffbd-booleen.png" width="42"/></td>
      <td valign="top"><strong>training_mode :</strong> <em><strong>boolean</strong></em>, whether the layer is in training mode (can store data for backward).</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “False”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Double.Png" src="/_assets/shared-images/96/9619568f4a4a-double.png" width="42"/></td>
      <td valign="top"><strong>lda coeff :</strong> <em><strong>float</strong></em>, defines the coefficient by which the loss derivative will be multiplied before being sent to the previous layer (since during the backward run we go backwards).</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “1”.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name (optional) :</strong> <em><strong>string,</strong></em> name of the node.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="param_node_layer_norm" src="assets/param_node_layer_norm.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="42"/></td>
      <td valign="top"><strong>Graphs out :</strong> <strong><em>cluster,</em></strong> ONNX model architecture.</td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>Y (heterogeneous) – T : <em>object, </em></strong>normalized tensor.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>Mean (optional, heterogeneous) – U : <em>object, </em></strong>saved mean used during training to speed up gradient computation.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>InvStdDev (optional, heterogeneous) – U : <em>object, </em></strong>saved inverse standard deviation used during training to speed up gradient computation.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_node_layer_norm" src="assets/output_node_layer_norm.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Type Constraints</h2>

<p><strong>T</strong> in (<code>tensor(bfloat16)</code>, <code>tensor(double)</code>, <code>tensor(float)</code>, <code>tensor(float16)</code>) : Constrain input types and output Y type to float tensors.</p>

<p><strong>U</strong> in (<code>tensor(bfloat16)</code>, <code>tensor(float)</code>) : Type of Mean and InvStdDev tensors.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
