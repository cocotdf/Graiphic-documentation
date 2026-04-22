<h1>SeparableConv1D</h1>

<h2>Description</h2>

<p>Adds the weights of the SeparableConv1D layer to the weights table. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="separable_conv_1d_format_by_name.PNG" src="/_assets/shared-images/dd/dd6c6ec6864b-separable_conv_1d_format_by_name.png" width="301"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td valign="top" width="70%"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Cluster Array In.Png" src="/_assets/shared-images/7c/7c2884d81fe7-cluster-array-in.png" width="42"/></td>
      <td valign="top"><strong>Weights in : array</strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>, </strong>name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="var-in.png" src="/_assets/shared-images/b5/b57556fba564-var-in.png" width="42"/></td>
      <td valign="top"><strong>weights : <em>variant,</em></strong> weights values.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="weights_in_by_name" src="/_assets/shared-images/ef/ef70b5a40eb8-weights_in_by_name.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>, </strong>name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>filters_depthwise : <em>array, </em></strong>3D values. filters_depthwise = [channels, 1, size].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>filters_pointwise : <em>array, </em></strong>3D values. filters_pointwise = [n_filters, channels, 1].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>biases : <em>array, </em></strong>1D values. biases = [n_filters].</td>
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
      <td width="64" valign="top"><img alt="Cluster Array Out.Png" src="/_assets/shared-images/ce/ce79fc3283cc-cluster-array-out.png" width="42"/></td>
      <td valign="top"><strong>Weights out : array</strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="String Out.Png" src="/_assets/shared-images/19/19b639e10167-string-out.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>, </strong>name of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="var-out.png" src="/_assets/shared-images/d7/d706fcdab793-var-out.png" width="42"/></td>
      <td valign="top"><strong>weights : <em>variant,</em></strong> weights values.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="weights_out_by_name" src="/_assets/shared-images/8c/8c5c7effb5f0-weights_out_by_name.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>filters_depthwise = [channels, 1, size]</li>
</ul>

<p>The size of filters_depthwise depends on the input of the <a href="../../../../architecture/layers/separable-conv-1d-add-to-graph/README.md">SeparableConv1D</a> layer and the parameters size.<br/>For example if the input of the layer has a size of [batch_size = 10, channels = 5, steps = 2] and size the value 3 then filters_depthwise will have a size of [channels = 5, 1, size = 3].</p>

<ul>
<li>filters_pointwise = [n_filters, channels, 1]</li>
</ul>

<p>The size of filters_pointwise depends on the input of the <a href="../../../../architecture/layers/separable-conv-1d-add-to-graph/README.md">SeparableConv1D</a> layer and the parameters n_filters.<br/>For example if the input of the layer has a size of [batch_size = 10, channels = 5, steps = 2] and n_filters has the value 6 then filters_pointwise will have a size of [n_filters = 6, channels = 5, 1].</p>

<ul>
<li>biases = [n_filters]</li>
</ul>

<p>The size of biases depends on the parameter n_filters of the <a href="../../../../architecture/layers/separable-conv-1d-add-to-graph/README.md">SeparableConv1D</a> layer.</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
