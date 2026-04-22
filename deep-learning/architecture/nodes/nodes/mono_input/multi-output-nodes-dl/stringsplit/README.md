<h1>StringSplit</h1>

<h2>Description</h2>

<p>StringSplit splits a string tensor’s elements into substrings based on a delimiter attribute and a maxsplit attribute.</p>

<p align="center"><img alt="node_string_split.png" src="/_assets/shared-images/4e/4eb79356d538-node_string_split.png" width="311"/></p>

<p>The first output of this operator is a tensor of strings representing the substrings from splitting each input string on the <code>delimiter</code> substring. This tensor has one additional rank compared to the input tensor in order to store the substrings for each input element (where the input tensor is not empty). Note that, in order to ensure the same number of elements are present in the final dimension, this tensor will pad empty strings as illustrated in the examples below. Consecutive delimiters are not grouped together and are deemed to delimit empty strings, except if the <code>delimiter</code> is unspecified or is the empty string (“”). In the case where the <code>delimiter</code> is unspecified or the empty string, consecutive whitespace characters are regarded as a single separator and leading or trailing whitespace is removed in the output.</p>

<p>The second output tensor represents the number of substrings generated. <code>maxsplit</code> can be used to limit the number of splits performed – after the <code>maxsplit</code>th split if the string is not fully split, the trailing suffix of input string after the final split point is also added. For elements where fewer splits are possible than specified in <code>maxsplit</code>, it has no effect.</p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_String.Png" src="/_assets/shared-images/60/600c0aac18dc-input_array_string.png" width="42"/></td>
      <td valign="top"><strong><a href="../../../../../../more-deep-learning/nodes-parameters/specified_outputs_name/README.md">specified_outputs_name</a> : <em>array, </em></strong>this parameter lets you manually assign custom names to the output tensors of a node.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>X (heterogeneous) – T1 : <em>object, </em></strong>tensor of strings to split.</td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="32"/><strong>Parameters : <em>cluster,</em></strong></p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>delimiter : <em>string,</em></strong> delimiter to split on. If left unset or set to the empty string (“”), the input is split on consecutive whitespace.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>maxsplit : <em>integer,</em></strong> maximum number of splits (from left to right). If left unset (or if the number of possible splits are less than maxsplit), it will make as many splits as possible. Note that the maximum possible number of substrings returned with <code>maxsplit</code> specified is <code>maxsplit+1</code> since the remaining suffix after the <code>maxsplit</code>th split is included in the output.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “0”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Booleen.Png" src="/_assets/shared-images/e9/e9f30799ffbd-booleen.png" width="42"/></td>
      <td valign="top"><strong>training? :</strong> <em><strong>boolean</strong></em>, whether the layer is in training mode (can store data for backward).</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “True”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Double.Png" src="/_assets/shared-images/96/9619568f4a4a-double.png" width="42"/></td>
      <td valign="top"><strong>lda coeff :</strong> <em><strong>float</strong></em>, defines the coefficient by which the loss derivative will be multiplied before being sent to the previous layer (since during the backward run we go backwards).</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “1”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name (optional) :</strong> <em><strong>string,</strong></em> name of the node.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="param_node_string_split" src="assets/param_node_string_split.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><p><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="32"/><strong>Graphs out :</strong><strong><em>cluster,</em></strong> ONNX model architecture.</p>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>Y (heterogeneous) – T2 : <em>object, </em></strong>tensor of substrings representing the outcome of splitting the strings in the input on the delimiter. Note that to ensure the same number of elements are present in the final rank, this tensor will pad any necessary empty strings.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>Z (heterogeneous) – T3 : <em>object, </em></strong>the number of substrings generated for each input element.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_node_string_split" src="assets/output_node_string_split.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Type Constraints</h2>

<p><strong>T1</strong> in (<code>tensor(string)</code>) : The input must be a UTF-8 string tensor</p>

<p><strong>T2</strong> in (<code>tensor(string)</code>) : Tensor of substrings.</p>

<p><strong>T3</strong> in (<code>tensor(int64)</code>) : The number of substrings generated.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
