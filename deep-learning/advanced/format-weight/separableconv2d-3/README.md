<h1>SeparableConv2D</h1>

<h2>Description</h2>

<p>Returns the SeparableConv2D layer weights. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="separable_conv_2d_format.png" src="/_assets/shared-images/2f/2fcbeb7d2e15-separable_conv_2d_format.png" width="233"/></p>

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
      <td valign="top"><strong>filters_depthwise : <em>array, </em></strong>4D values. filters_depthwise = [channels, 1, size[0], size[1]].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>filters_pointwise : <em>array, </em></strong>4D values. filters_pointwise = [n_filters, channels, 1, 1].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>biases : <em>array, </em></strong>1D values. biases = [n_filters].</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="separable_conv_2d_weights_info" src="/_assets/shared-images/11/11944c237a1b-separable_conv_2d_weights_info.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>filters_depthwise = [channels, 1, size[0], size[1]]</li>
</ul>

<p>The size of filters_depthwise depends on the input of the <a href="../../../architecture/layers/separable-conv-2d-add-to-graph/README.md">SeparableConv2D</a> layer and the parameters size.<br/>For example if the input of the layer has a size of [batch_size = 10, channels = 5, rows = 2, cols = 2] and size the value [3, 3] then filters_depthwise will have a size of [channels = 5, 1, size[0] = 3, size[1] = 3].</p>

<ul>
<li>filters_pointwise = [n_filters, channels, 1, 1]</li>
</ul>

<p>The size of filters_pointwise depends on the input of the <a href="../../../architecture/layers/separable-conv-2d-add-to-graph/README.md">SeparableConv2D</a> layer and the parameters n_filters. <br/>For example if the input of the layer has a size of [batch_size = 10, channels = 5, rows = 2, cols = 2] and n_filters has the value 6 then filters_pointwise will have a size of [n_filters = 6, channels = 5, 1, 1].</p>

<ul>
<li>biases = [n_filters]</li>
</ul>

<p> The size of biases depends on the parameter n_filters of the <a href="../../../architecture/layers/separable-conv-2d-add-to-graph/README.md">SeparableConv2D</a> layer.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
