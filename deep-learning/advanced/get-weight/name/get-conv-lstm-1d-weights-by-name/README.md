<h1>ConvLSTM1D</h1>

<h2>Description</h2>

<p>Gets the weights of the ConvLSTM1D layer selected by the name. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="/_assets/shared-images/23/2365c3ecb500-get_weights_by_name.png" alt="Get_Weights_By_Name.Png" width="240" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String.Png" src="/_assets/shared-images/c7/c7f7e539d8ca-string.png" width="42"/></td>
      <td valign="top"><strong>name : <em>string</em>, </strong>name of layer.</td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Model.Png" src="/_assets/shared-images/3c/3c881c79a647-output_model.png" width="42"/></td>
      <td valign="top"><strong>Model out : </strong>model architecture.</td>
    </tr>
  </tbody>
</table>

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
      <td valign="top"><strong>kernel : <em>array, </em></strong>3D values. kernel = [4*n_filters, channels, size].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>recurrent_kernel : <em>array, </em></strong>3D values. recurrent_kernel = [4*n_filters, n_filters, size].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>bias : <em>array, </em></strong>1D values. bias = [4*n_filters].</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img src="/_assets/shared-images/de/def0d4a513a5-conv_lstm_1d_weights_info.png" alt="conv_lstm_1d_weights_info" width="159" /></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>kernel = [4*n_filters, channels, size]</li>
</ul>

<p>The kernel size depends on the input of the <a href="../../../../architecture/layers/conv-lstm-1d-add-to-graph/README.md">ConvLSTM1D</a> layer and the parameters n_filters and size of the ConvLSTM1D cell.<br/>
For example, if the input of the layer has a size of [samples = 10, time = 8, channels = 5, rows = 2], n_filters a value of 6 and size the value 3, then kernel will have a size of [4*n_filters = 6, channels = 5, size = 3].</p>

<ul>
<li>recurrent_kernel = [4*n_filters, n_filters, size].</li>
</ul>

<p>The size of recurrent_kernel depends on the parameters n_filters and size of the ConvLSTM1D cell.<br/>
For example, if n_filters has a value of 6 and size the value 3, then recurrent_kernel will have a size of [4*n_filters = 6, n_filters = 6, size = 3].</p>

<ul>
<li>bias = [4*n_filters].</li>
</ul>

<p>The size of bias depends on the parameter n_filters of the ConvLSTM1D cell.<br/>
For example, if n_filters has a value of 6 then the bias size will be [4*n_filters = 6].</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
