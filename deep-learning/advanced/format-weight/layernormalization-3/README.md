<h1>LayerNormalization</h1>

<h2>Description</h2>

<p>Returns the LayerNormalization layer weights. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="layer_norm_format.png" src="/_assets/shared-images/97/97b131b8f9d5-layer_norm_format.png" width="233"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster.Png" src="/_assets/shared-images/0b/0bc4128edda1-cluster.png" width="42"/></td>
      <td valign="top"><strong>weights : cluster</strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer, </em></strong>index of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string, </em></strong>name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="var-in.png" src="/_assets/shared-images/b5/b57556fba564-var-in.png" width="42"/></td>
      <td valign="top"><strong>weight : <em>variant, </em></strong>weight of layer.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_weight_format" src="/_assets/shared-images/60/605463a40898-input_weight_format.png" width="220"/></p></td>
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
      <td valign="top"><strong>weights_info : cluster</strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer, </em></strong>index of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string, </em></strong>name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Cluster Out.Png" src="/_assets/shared-images/0a/0a479d27b394-cluster-out.png" width="42"/></td>
      <td valign="top"><strong>weights : cluster</strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>gamma : <em>array, </em></strong>1D values. gamma = [input_dim1].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>beta : <em>array, </em></strong>1D values. beta = [input_dim1].</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="layer_norm_weights_info" src="/_assets/shared-images/c5/c5f364582fcb-layer_norm_weights_info.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>gamma = [input_dim1]</li>
</ul>

<p>The size depends on the input to the <a href="../../../architecture/layers/layer-norm-add-to-graph/README.md">LayerNormalization</a> layer.<br/>For example, if the layer input has a size of [batch_size = 10, input_dim1 = 5, input_dim2 = 4, input_dim3 = 2] then gamma will have a size of [input_dim1 = 5].<br/>Another example, if the input of the layer has a size of [batch_size = 12, input_dim1 = 8, input_dim2 = 5, input_dim3 = 3] then gamma will have a size of [input_dim1 = 8].</p>

<ul>
<li>beta = [input_dim1]</li>
</ul>

<p>The beta size is based on the same principle as the gamma size.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
