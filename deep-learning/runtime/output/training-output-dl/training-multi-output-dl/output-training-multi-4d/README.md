<h1>4D</h1>

<h2>Description</h2>

<p>Retrieve a 4D output tensor (Bool, Int/UInt, Float, or String) from a list of outputs, using its index (Training Session). Type : <em><strong>polymorphic</strong><strong>.</strong></em></p>

<p align="center"><img src="assets/output_training_multi_4d.png" alt="output_training_multi_4d" width="260" /></p>

<h3>Input parameters</h3>

<table>
  <tbody>
    <tr>
      <td width="64" valign="top"><img alt="Input_Training.Png" src="/_assets/shared-images/b9/b9b04fd7d3fc-input_training.png" width="42"/></td>
      <td valign="top"><strong>Training in</strong> <strong>: <em>object, </em></strong>training session.</td>
    </tr>
    <tr>
      <td width="64" valign="top"><img alt="Integer 32.Png" src="/_assets/shared-images/6c/6c9e54b4bc43-integer-32.png" width="42"/></td>
      <td valign="top"><strong>index : </strong><i><strong>integer</strong></i><strong>,</strong> defines the position of the output within the data array. It corresponds to the index assigned to the output when it is created (via the <i>index</i> parameter).</td>
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
    <tr>
      <td width="64" valign="top"><img alt="Array Single Out.Png" src="/_assets/shared-images/fd/fdf478605b09-array-single-out.png" width="42"/></td>
      <td valign="top"><strong>4D Output Data : <em>array</em>, </strong>4D array of data with any type : integers (signed/unsigned), floats, doubles, booleans, or strings.​</td>
    </tr>
  </tbody>
</table>

<h2>Example</h2>

<p>All these exemples are snippets PNG, you can drop these Snippet onto the block diagram and get the depicted code added to your VI (Do not forget to install Deep Learning library to run it).</p>
