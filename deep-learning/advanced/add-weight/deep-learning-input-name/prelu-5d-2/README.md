<h1>PReLU 5D</h1>

<h2>Description</h2>

<p>Adds the weight of the PReLU5D layer to the weights table. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="prelu_5d_format_by_name.PNG" src="/_assets/shared-images/ed/ed22e41e8e23-prelu_5d_format_by_name.png" width="246"/></p>

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
      <td valign="top"><strong>alpha : <em>array, </em></strong>4D alpha values. alpha = [input_dim1, input_dim2, input_dim3, input_dim4].</td>
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
<li>alpha = [input_dim1, input_dim2, input_dim3, input_dim4]</li>
</ul>

<p>Its size depends on the input of the <a href="../../../../architecture/layers/prelu-add-to-graph/README.md">PReLU</a> layer.<br/>For example, if the layer has an entry [batch_size = 10, input_dim1 = 7, input_dim2 = 5, input_dim3 = 3, input_dim4 = 2] then alpha will have a size [input_dim1 = 7, input_dim2 = 5, input_dim3 = 3, input_dim4 = 2].<br/>The size can also depend on the “shared_axis” parameter that you set to the <a href="../../../../architecture/layers/prelu-add-to-graph/README.md">PReLU</a> layer. Each axis specified in this param is represented by a 1 in the weights.<br/>For example, if you set the parameter with the values [2], alpha will have a size [input_dim1 = 7, 1, input_dim3 = 3, input_dim4 = 2].<br/>Another example, if you define the parameter with the values [2, 3], alpha will have a size [input_dim1 = 7, 1, 1, input_dim4 = 2].</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
