<h1>BifurcationDetector</h1>

<h2>Description</h2>

<p>Component for aggressive decoding. Find the bifurcation index of predicted tokens, between source tokens, starting from previous suffix match index, and predicted tokens. Concat predicted tokens, starting from bifurcation index, to the back of current tokens. This forms the output tokens. Detect suffix match index in source tokens, between source tokens and output tokens. Detection is based on finding the appearances of last n-gram in output tokens in source tokens. A match is considered found if source tokens contain a single matching n-gram. Return the index of the start of the n-gram in source tokens. No matching if found if src tokens contain multiple or zero matching n-grams. Return -1.</p>

<p align="center"><img alt="BifurcationDetector" src="assets/BifurcationDetector.png" width="311"/></p>

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
      <td valign="top"><strong>src tokens – T : <em>object, </em></strong>encoder input ids.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>cur tokens – T : <em>object, </em></strong>decoder input ids.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>prev suffix match idx – T : <em>object, </em></strong>previous suffix match index.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Object_3.Png" src="/_assets/shared-images/1b/1bd436ec7533-input_object_3.png" width="42"/></td>
      <td valign="top"><strong>pred tokens – T : <em>object, </em></strong>predicted token ids from aggressive decoding.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_node_bifurcation_detector" src="assets/input_node_bifurcation_detector.png" width="220"/></p></td>
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
      <td width="64" valign="top"><img alt="node_bifurcation_detector.png" src="/_assets/shared-images/15/157eeddc386a-node_bifurcation_detector.png" width="42"/></td>
      <td valign="top"><strong>max ngram size : <em>integer,</em></strong> the maximum NGram size for suffix matching.</td>
    </tr>
    <tr>
      <td width="64" valign="top"></td>
      <td valign="top">Default value “0”.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Image Missing.Svg" src="../../../../../../../_assets/image-missing.svg" width="42"/></td>
      <td valign="top"><strong>min ngram size :</strong> <strong><em>integer</em></strong>, the minimum NGram size for suffix matching.</td>
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
  </tbody>
</table></td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name (optional) :</strong> <em><strong>string,</strong></em> name of the node.</td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="param_node_bifurcation_detector" src="assets/param_node_bifurcation_detector.png" width="220"/></p></td>
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
      <td valign="top"><strong>tokens – T : <em>object, </em></strong>decoder input ids after merging predicted tokens.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Object_3.Png" src="/_assets/shared-images/e2/e2d605658777-output_object_3.png" width="42"/></td>
      <td valign="top"><strong>suffix_match_idx – T : <em>object, </em></strong>new suffix match index.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_node_bifurcation_detector" src="assets/output_node_bifurcation_detector.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Type Constraints</h2>

<p><strong>T</strong> in (<code>tensor(int64)</code>) : Constrain to integer types.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
