<h1>ConvLSTM2D</h1>

<h2>Description</h2>

<p>Adds the weights of the ConvLSTM2D layer to the weights table. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="conv_lstm_2d_format_by_index.PNG" src="/_assets/shared-images/4b/4b50a7546190-conv_lstm_2d_format_by_index.png" width="293"/></p>

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
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer,</em></strong> index of layer.</td>
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
      <td valign="top" width="30%"><p align="center"><img alt="weights_in_by_index" src="/_assets/shared-images/9a/9a22bf92b788-weights_in_by_index.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>, </strong>index of layer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>kernel : <em>array, </em></strong>4D values. kernel = [4*n_filters, channels, size[0], size[1]].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>recurrent_kernel : <em>array, </em></strong>4D values. recurrent_kernel = [4*n_filters, n_filters, size[0], size[1]].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single.Png" src="/_assets/shared-images/f8/f8cc8ee3265a-array-single.png" width="42"/></td>
      <td valign="top"><strong>bias : <em>array, </em></strong>1D values. bias = [4*n_filters].</td>
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
      <td width="64" valign="top"><img alt="Integer 32 Out.Png" src="/_assets/shared-images/c8/c80fd0f5f3d5-output_interger_32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer,</em></strong> index of layer.</td>
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
      <td valign="top" width="30%"><p align="center"><img alt="weights_out_by_index" src="/_assets/shared-images/83/8330633273f9-weights_out_by_index.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>kernel = [4*n_filters, channels, size[0], size[1]]</li>
</ul>

<p>The kernel size depends on the input of the <a href="../../../../architecture/layers/conv-lstm-1d-add-to-graph/README.md">ConvLSTM2D</a> layer and the parameters n_filters and size of the ConvLSTM2D cell.<br/>For example, if the input of the layer has a size of [samples = 10, time = 8, channels = 5, rows = 3, cols = 2], n_filters a value of 6 and size the value [3, 3], then kernel will have a size of [4*n_filters = 6, channels = 5, size[0] = 3, size[1] = 3].</p>

<ul>
<li>recurrent_kernel = [4*n_filters, n_filters, size[0], size[1]]</li>
</ul>

<p>The size of recurrent_kernel depends on the parameters n_filters and size of the ConvLSTM2D cell.<br/>For example, if n_filters has a value of 6 and size the value [3, 3], then recurrent_kernel will have a size of [4*n_filters = 6, n_filters = 6, size[0] = 3, size[1] = 3].</p>

<ul>
<li>bias = [4*n_filters]</li>
</ul>

<p>The size of bias depends on the parameter n_filters of the ConvLSTM2D cell.<br/>For example if n_filters has a value of 6 then the bias size will be [4*n_filters = 6].</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
