<h1>SimpleRNN</h1>

<h2>Description</h2>

<p>Gets the weights of the SimpleRNN selected by the index. Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img alt="SimpleRNN" src="assets/SimpleRNN.png" width="240"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Model.Png" src="/_assets/shared-images/21/21498ef0ddd0-input_model.png" width="42"/></td>
      <td valign="top"><strong>Model in : </strong>model architecture.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : <em>integer</em>, </strong>index of layer.</td>
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
      <td valign="top"><strong>input_weights : <em>array, </em></strong>2D values. input_weights = [features, units].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>hidden_weights : <em>array, </em></strong>2D values. hidden_weights = [units, units].</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>biases : <em>array, </em></strong>1D values. biases = [units].</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="simple_rnn_weights_info" src="/_assets/shared-images/0c/0cabed38dc97-lstm_weights_info.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Dimension</h2>

<ul>
<li>input_weights = [features, units]</li>
</ul>

<p>The size depends on the <a href="../../../../architecture/layers/simple-rnn-add-to-graph/README.md">SimpleRNN</a> layer input and the units parameter. <br/>For example, if the input has a size of [batch = 10, timesteps = 8, features = 5] and units a value of 3 then input_weights will have a size of [features = 5, units = 3]. <br/>Another example, if the input has a size of [batch = 15, timesteps = 8, features = 6] and units a value of 2 then input_weights will have a size of [features = 6, units = 2].</p>

<ul>
<li>hidden_weights = [units, units]</li>
</ul>

<p>The size depends on the units parameter of the <a href="../../../../architecture/layers/simple-rnn-add-to-graph/README.md">SimpleRNN</a> layer.<br/>For example, if units has a value of 6 then hidden_weights will have a size of [units = 6, units = 6]. <br/>Another example, if units has a value of 2 then hidden_weights will have a size of [units = 2, units = 2].</p>

<ul>
<li>biases = [units]</li>
</ul>

<p>The size depends on the units parameter of the <a href="../../../../architecture/layers/simple-rnn-add-to-graph/README.md">SimpleRNN</a> layer. <br/>For example, if units has a value of 6, then biases will have a size of [units = 6]. <br/>Another example, if units has a value of 2, then biases will have a size of [units = 2].</p>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
