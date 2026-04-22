<h1>Inputs CPU Raw Data</h1>

<h2>Description</h2>

<p>Runs a full training step on the model with raw input data from the CPU. This includes the forward and backward pass, followed by the optimizer update and gradient reset (only if the weights are updated). The output buffer is allocated automatically.</p>

<p align="center"><img alt="training_full_train_step_cpu" src="/_assets/shared-images/07/0799a1bbeaa2-training_full_train_step_cpu.png" width="220"/></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Training.Png" src="/_assets/shared-images/b9/b9b04fd7d3fc-input_training.png" width="42"/></td>
      <td valign="top"><strong>Training in</strong> <strong>: <em>object, </em></strong>training session.</td>
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
      <td valign="top"><strong>Inputs Info : <em>cluster</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Unsigned_8.Png" src="/_assets/shared-images/f7/f7e8b09da0a0-input_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>inputs_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs_shapes :<em> array, </em>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs string length : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Integer_64.Png" src="/_assets/shared-images/71/712313814f21-input_array_integer_64.png" width="42"/></td>
      <td valign="top">inputs_ranks :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_Enum.Png" src="/_assets/shared-images/05/05126b56ff83-input_array_enum.png" width="42"/></td>
      <td valign="top">inputs_types :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Booleen.Png" src="/_assets/shared-images/e9/e9f30799ffbd-booleen.png" width="42"/></td>
      <td valign="top"><strong>update? :</strong> <i><strong>boolean,</strong></i> indicating whether to update the model weights at this step. If set to <code>false</code>, gradients are only accumulated without updating the weights.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="input_param_training_full_train_step_cpu" src="/_assets/shared-images/b3/b34224f8fa2c-input_param_training_full_train_step_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h3>Output parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Training.Png" src="/_assets/shared-images/2b/2b7b59c59760-output_training.png" width="42"/></td>
      <td valign="top"><strong>Training out</strong> <strong>: <em>object, </em></strong>training session.</td>
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
      <td valign="top"><strong>Losses Info : <em>cluster</em></strong></td>
    </tr>
    <tr>
      <td></td>
      <td valign="top"><table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Unsigned_8.Png" src="/_assets/shared-images/ee/eeb63aea4468-output_array_unsigned_8.png" width="42"/></td>
      <td valign="top"><strong>outputs_raw_data : <em>array, </em></strong>contains the raw byte representation of the input tensor data, stored as a 1D flattened buffer.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_shapes_array :<em> array, </em>specifies the shape of the input tensor. Since the data is stored as a flattened 1D buffer, this shape is necessary to reconstruct the original dimensions.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_strings_length_array : <em>array, </em>used when the tensor type is string. If the tensor has shape <code>[5,3]</code>, this field contains 15 values, each representing the length of a corresponding string element. This ensures that the actual size of <code>inputs_data</code> is known despite variable string lengths.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Integer_64.Png" src="/_assets/shared-images/8a/8a3ecb76444e-output_array_integer_64.png" width="42"/></td>
      <td valign="top">output_ranks_array :<em> array, </em>indicates the rank of the tensor, i.e. the number of dimensions (Scalar = 0, 1D = 1, 2D = 2, etc.).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Out Array Integer 32.Png" src="/_assets/shared-images/fe/fe7405762e7c-output_array_integer_32.png" width="42"/></td>
      <td valign="top">output_types_array :<em> array, </em>defines the ONNX tensor type as an enumerated value (e.g. FLOAT, INT64, STRING).</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="String_Array_Out.Png" src="/_assets/shared-images/43/43e33de4b021-output_array_string.png" width="42"/></td>
      <td valign="top"><strong>losses_names : <em>array,</em></strong> specifies which loss the data correspond to.</td>
    </tr>
  </tbody>
</table></td>
    </tr>
  </tbody>
</table></td>
      <td valign="top" width="30%"><p align="center"><img alt="output_param_training_full_train_step_cpu" src="/_assets/shared-images/ba/ba1e285bfea1-output_param_training_full_train_step_cpu.png" width="220"/></p></td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
