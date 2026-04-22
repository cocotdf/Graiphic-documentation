<h1>Initialize FIFO</h1>

<h2>Description</h2>

<p>Initializes an asynchronous FIFO used to store loss values during training.</p>

<p align="center"><img src="assets/asynchronous_fit_fifo_init.png" alt="asynchronous_fit_fifo_init" width="260" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Output_Array_Enum.Png" src="/_assets/shared-images/93/9363ce0bc3eb-output_array_enum.png" width="42"/></td>
      <td valign="top"><strong>FIFO Full Action : <em>enum,</em></strong> determines what happens when the FIFO buffer is full.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Training.Png" src="/_assets/shared-images/b9/b9b04fd7d3fc-input_training.png" width="42"/></td>
      <td valign="top"><strong>Training in</strong> <strong>: <em>object, </em></strong>training session.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Array_String.Png" src="/_assets/shared-images/60/600c0aac18dc-input_array_string.png" width="42"/></td>
      <td valign="top"><strong>Losses : <em>array,</em></strong> selects which loss values are written into the FIFO during training.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Input_Unsigned_64.Png" src="/_assets/shared-images/ee/ee44aaa4620b-input_unsigned_64.png" width="42"/></td>
      <td valign="top"><strong>capacity : <em>integer,</em></strong> defines the maximum number of records that can be stored in the FIFO buffer.</td>
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

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
